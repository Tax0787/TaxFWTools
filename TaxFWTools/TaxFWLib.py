class ClassFW:
    def __call__(self,*argv,mode='shell'):
        match mode:
            case 'shell':
                self.shell(*argv)
            case 'interperter':
                return self.interperter(*argv)
            case 'compile':
                return self.AOT(*argv)
            case 'JIT':
                return self.JIT(*argv)
            case 'VVM':
                return self.VVM(*argv)
            case 'help':
                self.help(*argv)
            case 'DOCS':
                self.DOCS(*argv)
            case 'env':
                self.enviroment(*argv)
            case 'PKG':
                self.pkg(*argv)
            case 'IDE':
                self.edit(*argv)
            case 'IDLE':
                self.idle(*argv)
            case 'Terminal':
                self.CLI(*argv)
            case 'GraphicUserTools':
                self.GUI(*argv)
            case 'IDS':
                self.ShellScriptEditer(*argv)
            case 'fetch':
                self.FetchFW(*argv)
            case 'updater':
                self.updater(*argv)
            case _:
                return self.mode(mode,*argv)
    def mode(self,mode:str,*argv):
        char='No More Mode'
        print(char)
        return char
    pass
