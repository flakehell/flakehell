# built-in
import json
from functools import partial

# external
from flake8.formatting.base import BaseFormatter

# app
from .._logic import make_baseline


category_complexity = "info"
category_bug = "critical"
category_style = "minor"
category_clarity = "info"
category_compatibility = "minor"

severity_info = 'info'
severity_minor = 'minor'
severity_major = 'major'
severity_critical = 'critical'
severity_blocker = 'blocker'


error_classes = {
    "C9": {
        "category": category_complexity,
        "severity": severity_info,
    },
    "E": {
        "category": category_style,
        "severity": severity_info,
    },
    "E7": {
        "category": category_clarity,
        "severity": severity_info,
    },
    "E9": {
        "category": category_bug,
        "severity": severity_major,
    },
    "F4": {
        "category": category_bug,
        "severity": severity_major,
    },
    "F6": {
        "category": category_bug,
        "severity": severity_major,
    },
    "F7": {
        "category": category_bug,
        "severity": severity_major,
    },
    "F8": {
        "category": category_bug,
        "severity": severity_major,
    },
    "W": {
        "category": category_style,
        "severity": severity_info,
    },
    "W6": {
        "category": category_compatibility,
        "severity": severity_minor,
    },
}


def _error_matching(error, key, fallback):
    code = error.code
    try:
        return error_classes[code][key]
    except KeyError:
        try:
            return error_classes[code[:2]][key]
        except KeyError:
            try:
                return error_classes[code[:1]][key]
            except KeyError:
                return fallback


error_category = partial(_error_matching,
                         key='category', fallback=category_clarity)
error_severity = partial(_error_matching,
                         key='severity', fallback=severity_info)


class GitlabFormatter(BaseFormatter):
    error_format = '{code} {text}'

    def start(self):
        super().start()
        self._write('[')
        self.newline = ''
        self._first_line = True

    def stop(self):
        self._write('\n]\n')
        super().stop()

    def handle(self, error):
        # redefined to never output source
        line = self.format(error)
        self._write(line)

    def format(self, error):
        filename = error.filename
        digest = make_baseline(
            path=filename,
            code=error.code,
            line=error.line_number,
            context=error.physical_line,
        )
        text = self.error_format.format(code=error.code, text=error.text)
        # docs.gitlab.com/ee/user/project/merge_requests/code_quality.html
        result = json.dumps(dict(
            description=text,
            fingerprint=digest,
            severity=error_severity(error),
            category=error_category(error),
            location={
                'path': filename,
                'lines': dict(begin=error.line_number),
            },
        ))
        if self._first_line:
            self._first_line = False
        else:
            result = ',\n' + result
        return result
