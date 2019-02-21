import copy
import yaml


class BaseChart:

    __slots__ = ['overrides']

    def __init__(self):
        # List of lambda functions which individually call an override function with its arguments
        self.overrides = []

    def withOverride(self, function, **kwargs):
        """Returns a brand new BaseChart

        Allows chaining: BaseChart().withOverride(func1, arg1a, arg1b).withOverride(...)
        """

        _copy = copy.deepcopy(self)
        _copy.overrides.append(lambda values: function(values, **kwargs))
        return _copy

    def withO(self, function, **kwargs):
        """Short Alias for self.withOverride"""
        return self.withOverride(function, **kwargs)

    def toYaml(self, debug=False):
        u = {}
        for override in self.overrides:
            u = override(u)
            if debug:
                print("#####\ngenerate", yaml.dump(u, default_flow_style=False))

        # Outputting the yaml has a problem with multi-line strings.
        #   Make multi-line strings come out as yaml block quotes
        #   https://stackoverflow.com/questions/45004464/yaml-dump-adding-unwanted-newlines-in-multiline-strings
        yaml.SafeDumper.org_represent_str = yaml.SafeDumper.represent_str

        def repr_str(dumper, data):
            if '\n' in data:
                return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
            return dumper.org_represent_str(data)

        yaml.add_representer(str, repr_str, Dumper=yaml.SafeDumper)

        return yaml.safe_dump(u, default_flow_style=False)
