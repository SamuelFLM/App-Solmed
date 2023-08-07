import abc


class IBackRegister(abc.ABC):
    @abc.abstractclassmethod
    def _main(self):
        pass
    