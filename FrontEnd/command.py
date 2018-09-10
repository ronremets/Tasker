# coding=ascii
"""
a command
"""
__author__ = "Ron Remets"


class Command(object):
    """
    a command
    """

    def __init__(self, text):
        self._args = Command._parse(text)

    def __len__(self):
        return len(self._args)

    def __getitem__(self, key):
        return self._args[key]

    def __setitem__(self, key, value):
        self._args[key] = value

    def __delitem__(self, key):
        del self._args[key]

    def __str__(self):
        output = ""
        for arg_num, (arg, value) in enumerate(self._args.items()):
            output += "Arg[{}]: {} = {}\n".format(arg_num, arg, value)
        return output

    def __repr__(self):
        output = ""
        output += self._args["command"] + '?'
        for arg, value in self._args.items():
            if arg != "command":
                output += "{}={}&".format(arg, value)
        if output.endswith('&'):
            output = output[:-1]
        print("REPR: {}".format(output))
        return output

    @staticmethod
    def _parse(text):
        """
        text = "command?arg1=value&arg2=value&arg3=value..."
        :param text:
        :return:
        """
        args = dict()
        args["command"] = text[:text.index('?')]
        for arg in text[text.index('?') + 1:].split('&'):
            args[arg[:arg.index('=')]] = arg[arg.index('=') + 1:]
        return args

    @staticmethod
    def iter_parse_task(tasks):
        output = ""
        for task_num, task in enumerate(tasks):
            output += "&task[{}]={}".format(task_num, str(task))
        return output
