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
        return yaml.dump(u, default_flow_style=False)
