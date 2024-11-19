class Control: #1
    _tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    def turnOn(self) -> None:
        self._tv.turnOn()

    def turnOff(self) -> None:
        self._tv.turnOff()

    def canalUp(self) -> None:
        self._tv.canalUp()
    
    def canalDown(self) -> None:
        self._tv.canalDown()

    def volumenUp(self) -> None:
        self._tv.volumenUp()

    def volumenDown(self) -> None:
        self._tv.volumenDown()

    def setCanal(self, canal: int) -> None:
        self._tv.setCanal(canal)

    def setVolumen(self, volumen: int) -> None:
        self._tv.setVolumen(volumen)

    
        