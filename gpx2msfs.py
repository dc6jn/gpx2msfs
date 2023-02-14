#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# msfs gpx import script
# this script reads gpx files and output a project for MSFS2020 wich contains wypoints as POI visible during flight as a virtual path
# Copyright (c) 2023 dc6jn
# "c:\Program Files\GPSBabel\gpsbabel.exe" -i gpx -f "USA V4 mit Hotels.gpx" -w -r -t -x simplify,crosstrack,error=0.02k -o gpx -F USA_filtered.gpx
__manufacturer__ = "manu"
__creator__ = "creator"
__default_scenery_name__ = 'MyPOIs'

### nothing to change below this line
__version__ = "0.1.0"

#This is a base64 encoded version of the default thumbnail image, feel free to replace with a more meaningful ;)
Thumbnail_jpg = '''/9j/4AAQSkZJRgABAQEASABIAAD/4Qt2RXhpZgAASUkqAAgAAAAGABoBBQABAAAAVgAAABsBBQAB
AAAAXgAAACgBAwABAAAAAgAAADEBAgANAAAAZgAAADIBAgAUAAAAdAAAAGmHBAABAAAAiAAAAJoA
AABIAAAAAQAAAEgAAAABAAAAR0lNUCAyLjEwLjE0AAAyMDIwOjA2OjAyIDE0OjQ2OjQyAAEAAaAD
AAEAAAABAAAAAAAAAAgAAAEEAAEAAAAAAQAAAQEEAAEAAABpAAAAAgEDAAMAAAAAAQAAAwEDAAEA
AAAGAAAABgEDAAEAAAAGAAAAFQEDAAEAAAADAAAAAQIEAAEAAAAGAQAAAgIEAAEAAABoCgAAAAAA
AAgACAAIAP/Y/+AAEEpGSUYAAQEAAAEAAQAA/9sAQwAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMP
FB0aHx4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy/9sAQwEJCQkMCwwYDQ0YMiEc
ITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy/8AAEQgA
aQEAAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMC
BAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYn
KCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeY
mZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5
+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwAB
AgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpD
REVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ip
qrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMR
AD8A6OiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo
oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii
igAooooAKKKKACiiigAooooAKKKKAClVdxxkD60lWbC0+3X8NqH2eY2N2M4/CgCLyv8AbT86PK/2
0/OunbwYqttbU0BPYxf/AGVZWsaDcaQFkZ1lhY4DqMYPoRQBm+V/tp+dHlf7afnWrrWgHR4onNyJ
vMYjGzbj9TWNQBJ5X+2n50eV/tp+dTabYtqN/Faq20uTlsZwAM5rR1nw6+kW8c/2gTKz7T8m3HGf
U+lAGR5X+2n50eV/tp+dWNN02fVLsQQADjLMeij1rf8A+ENQkoupKZQM7fL/APr0Acx5X+2n50eV
/tp+dXl0addZTTZz5bs2A+Mgj1HqK2G8Gqhw2qIp9DFj/wBmoA5nyv8AbT86PK/20/OtTWNCTSrd
JVvUnLPt2quMcZz1NUtSsf7OvWtjJ5mFU7sY6jNAEHlf7afnR5X+2n51PBZefp15d+Zt+zbPl253
bjjr2qTTtLN8ks0ky29rEPnlYZwfQDuaAKnlf7afnR5X+2n51qx6NaXgdNO1ET3CgsIniKbsehNV
NL046lfi18zyjtJJK5xj2oAq+V/tp+dHlf7afnUferOn2n2+/htQ+zzDjdjOOPSgCLyv9tPzo8r/
AG0/OtV9K0yORo21pQ6kqR9mbgj8ap6lpsumyorsskci745U+64oAreV/tp+dHlf7afnWxcaHY2b
rHc6uI5Cobb9nJ4P0NVLqy0+G3Z4NUE8gxiPyGXP4k0AUvK/20/Ojyv9tPzrTt9ItW0yK9ur/wCz
rIxUDyi3I+hpTosE8Er6fqC3TxLvaIxlGx3Iz1oAyCMHGQfpSUUUAFFFFABRRRQAVpeH/wDkPWf+
/wD0NZtaXh//AJD1n/v/ANDQB0mv+HrvVNRWeB4QgjCnexBzk+3vTPEciWXhuHT5ZRLcEKvXnjqf
6fjVLxZd3MGrqkVxLGvkg4RyB1Nc07M5LMSzHqSck0Adl42/49bT/fb+VcZXofiHSJ9XhgSB40Mb
EneT6ewrmbzwreWVnLcyTQFIxkhSc/yoAveDLbDXV64wqrsU/qf6fnV2OdvEHhm8BTMqu+0Z7g7l
/TAp9obXRvCsRvFYpMvzqvVi/b8v5Uuhajo7XLW2nwSQvINxD9Gx+J55oAoeCAN18cc4T/2aucS8
mt9S+2K26ZZC+W7nPeuo0d4dJ8R6hYSMEWUgxE8D1A/Jv0psPg9k1QSyzRvaB92053EdcHtQBn2W
qT6r4lsZZ1jVlO0bARxya2tZ8NtqmoG5F0kQ2BdpXPT8azmNiPGFnFYRoqRna5ToW5q5rvhu61TU
jcwywqmwLhyc8fhQByN7bGzvJrYuHMbFdw710WtaNJeak063dnGGRPlll2sPlHbFZeq6Bc6TbpNN
JEys20BCc5xnuPaneJv+Q1J/uJ/6CKALn9mvp/hzVd9xby7zDjyX3Yw/f86qoceDZMd77B/74FMs
P+Rc1n6wf+h1Pp8R1Dw5cWMGGuUnE4jzgsuAOKAKOiEjW7Mg4PmgVraMMeMLkD+/N/M1W0XS7qLU
I7q5ie3t7c+Y7yqV6dhnrUvh+UXHimSZQQJPMYA++TQBz56mtLw9/wAh+z/3z/I0h0HVc/8AHjL+
VTaPbT2niS0iuI2jk3Z2t9DQBn3/APyEbr/rs/8AM1o6gS3hjSCSScyjJ9N1JeaHqct/cMlnIVaV
iD6gmn60q2mm6fpzOGnhV2lA/hLHOKANHXNHkvr2OZbq0iHkqNssu0/liubvbNrG48lpYpTgHdE2
4fnW/wCINLvrzUI5be2kkTyUG5R3rFuNJv7WFpp7WRI16sRwKANeOwe/8LWaJNBEVmc5lfaD16UW
diNAJ1C8uYWJjYQxxNu8wkY9OlVbr/kUrD/ru/8AWl0//iZaNcaceZoP38HPX+8v+fWgDEooooAK
KKKACiiigAp0ZYOGRtrDkHdjFNooAlk82Vt0km9umWkBP86b5beq/wDfQplFAFr7Tef8/cn/AH+/
+vTXmupFKvcuynqDLkH9ar0UATu88qhZJi6joGkyB+tMQSRuHRwrDoVcAj9ajooAlfzZW3SSb29W
kBP86kM90YfJNy5i6bPO4/LNVqKAJFWRGDI4Vh0IcAj9am+03n/P3J/3+/8Ar1VooAnke4mAEs5c
DkBpc/1pjiSRtzuGb1ZwT/Oo6KAJQJFRkDgK2NwDjBx680iCSNw6OFYcghwCP1qOigC1NcXlyoWe
6klUdA824fqaiTzYm3RyBG9VcA/zqKigC19pvP8An7k/7/f/AF6jLTtKJTMTIOjGTn881DRQBa+0
3h/5epP+/wB/9eoPLb1X/voUyigCyLi8AAF1IAP+m3/16R5bmRSslwzKeoaXI/nVeigCUiQoEMgK
A5C7xgfrQgkjYMjhWHdXAP8AOoqKAFIwcUlFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQA
UUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABR
RRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH/2f/iArBJQ0Nf
UFJPRklMRQABAQAAAqBsY21zBDAAAG1udHJSR0IgWFlaIAfkAAYAAgAMAA0AM2Fjc3BNU0ZUAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD21gABAAAAANMtbGNtcwAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADWRlc2MAAAEgAAAAQGNwcnQAAAFgAAAANnd0cHQA
AAGYAAAAFGNoYWQAAAGsAAAALHJYWVoAAAHYAAAAFGJYWVoAAAHsAAAAFGdYWVoAAAIAAAAAFHJU
UkMAAAIUAAAAIGdUUkMAAAIUAAAAIGJUUkMAAAIUAAAAIGNocm0AAAI0AAAAJGRtbmQAAAJYAAAA
JGRtZGQAAAJ8AAAAJG1sdWMAAAAAAAAAAQAAAAxlblVTAAAAJAAAABwARwBJAE0AUAAgAGIAdQBp
AGwAdAAtAGkAbgAgAHMAUgBHAEJtbHVjAAAAAAAAAAEAAAAMZW5VUwAAABoAAAAcAFAAdQBiAGwA
aQBjACAARABvAG0AYQBpAG4AAFhZWiAAAAAAAAD21gABAAAAANMtc2YzMgAAAAAAAQxCAAAF3v//
8yUAAAeTAAD9kP//+6H///2iAAAD3AAAwG5YWVogAAAAAAAAb6AAADj1AAADkFhZWiAAAAAAAAAk
nwAAD4QAALbEWFlaIAAAAAAAAGKXAAC3hwAAGNlwYXJhAAAAAAADAAAAAmZmAADypwAADVkAABPQ
AAAKW2Nocm0AAAAAAAMAAAAAo9cAAFR8AABMzQAAmZoAACZnAAAPXG1sdWMAAAAAAAAAAQAAAAxl
blVTAAAACAAAABwARwBJAE0AUG1sdWMAAAAAAAAAAQAAAAxlblVTAAAACAAAABwAcwBSAEcAQv/b
AEMAAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB
AQEBAQEBAQEBAf/bAEMBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB
AQEBAQEBAQEBAQEBAQEBAQEBAQEBAf/CABEIAKoBnAMBEQACEQEDEQH/xAAdAAEAAgMBAQEBAAAA
AAAAAAAABwgEBQYDCQIB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEAMQAAABsYAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAfs3oAAAAAAAAAAAAAAAAAABhmrAAAAABvj3NMfgzDVAG5MUwD0
OuOWP6bsGAeBgGSeQOwORPwZRhA3JmGgPM6MGEeZujUGoAAAAAAPpiR8SSVAJhKSAH06IdKTn0MO
fO9KgFyiMSJDZlYSXTjCxhE5LRWkmYruC3xGhK5VYtiRAcuSuccd4QYcKAAAAAD6YlMy2BApIBSQ
EhFvDtj5mn03PmMS0bQtKV9K2ltCISSCDCdCsJasrsTMV3BZ8rAWHIzLBkKkVloiMyQCLCPAAAAA
AfTEgcjw0BYQpIC3B0RI5TIvMfMUmo9iypW4goteQoSYQ0ToVhLVFdyZiu4LPlYCw5GZPBBxHpaI
iYmkqaAAAAAAfTE+cRqyVy8pGZE5ZQrcd2YR2J7G+Kkl0CNyIDNKwkunGFiiKyVitZbMiM4MsGRw
SiVWLaERnKkplZSciMzkQAAAAAbY1R/D2NqDEMg056maa06A0R6G0BiHiYp7nmDqDmD8m5BgnqZJ
qD8G6BiniYh+j3MYAAAAA/RtgAAAAAAAAAAAAAAAAAADGMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAH/8QAKxAAAAYCAQIGAgMBAQAAAAAAAAIDBAUGARQHFTUQFhcwNDYRNxITgCEz/9oACAEBAAEF
Av8AOJcfyNpIDSQGkgNJAaSA0kBpIDSQGkgNJAaSA0kBpIDSQGkgNJAaSA0kBpIDSQGkgNJAaSA0
kBpIDSQGkgNJAaSA0kBpIDSQGkgNJAaSA0kBpIDSQGkgFm6aRfcTipRYnRpgLt3DY6SKrhRwwfNC
+KMdIuSOGrpoYEIdQ3l2ezhVFVuoigs4U6NMDo0wHDB80Lhq6MgEUVnChyHTOQh1D+XJ/wDCiaiR
ylMYy7Zy1P4IR0g5J0aYCiaiR8YznPRpgdGmAvHyDUjVk8em6BOBzHv2fvVb66fkeCTWyWGtMXXY
80VfuTu0eNfYYiITkyOwtGipV1rBxqnJMERzMw0daI2ikOlbJ6wsq8j6mQIuNujrBHtP1kKJ9qne
+xmGlOrHnu0f3ustbvW4fu3JfffCIknMRx36iWQRT9rfmMeQ6UtdLVLQcp6iWQS1smJtrxf81S/2
Up6/dnEq8ssViFmvcq3111S7Oo6pkG5gYlm7Sfcncndo8KrH4kp+/wAnmPhHBUrHXc4yXNg/5XAx
u07HMaQsdxbrdXXFibL8aSaKIhmTqR478kWkVGrT0dYJ3vtw+pjjn4MP3bkvvvgn+rhxn3/P2i91
2al5fyTafDi/5qlMs+VKzTJNvJWqUTmJz3Kt9dX5NWRWl+QJeTQo32vk7tHhxhHZF4gZ2dd1FnJx
0Nc47p1in8ZPXRG0OZlGFKRM2uF1n38A1V5DsKyQiXbhjxz5ssYp9hmn1ine+3D6kOOfgw/duS++
+Cf6uHGff8/aL9Ny0bMebLH4cX/NUtdjwpNrL2em+7Vvrr75oo32ubgmU+39Nq+LjUYqBi6tH4io
Bfk2UwtV7y7mpXk6PwdrTrQ0lWCnHtcUcz9hj60wohjHtU5AMbAl6bV8XOpxkBHtP1kKJ9qne+xZ
mlxrHkO0f3PNWk1uH7tcqnLTsn6cWMTdcka+IeMczHHnpxYxGsWdAYx5zKS1zqctOynpxYxMVGXg
2vGHzVf/AFoMoRtIzsUeFlPcI/fJl8E1FEj9SkR1KRCrt24L1B/+AQ50jKvXi5QWWlSlMYxzJqqI
n6lIjqUiFXbpxjC6+EgmooicxjHMUxiG67Ofg5zqGxnJc9SkR1KRCzly4CT14gXqUiDnOobGfwOp
SI6lIhV47XKk4Xb5GM5LlVZZc3t4z/HO6cbpxunG6cbpxunG6cbpxunG6cbpxunG6cbpxunG6cbp
xunG6cbpxunG6cbpxunG6cbpxunG6cbpxunG6cbpxunG6cbpxunG6cbpxunCrgypf85f/8QAFBEB
AAAAAAAAAAAAAAAAAAAAoP/aAAgBAwEBPwEPH//EABQRAQAAAAAAAAAAAAAAAAAAAKD/2gAIAQIB
AT8BDx//xABLEAACAQIEAQgECQgJAwUAAAABAgMEEQAFEiETFDEzNZKU0tUQIkFRFSMyYXR1tLXT
BjBScXKys9QgJDRCQ0Vic4F2gIREZIKT0f/aAAgBAQAGPwL/ALcVUsqAkAu+rSlz8ptCu+lec6Ed
rfJVjtjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot
8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5Pj
rfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T
463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnP
k+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZz5PjrfK+xnPk+Ot8r7Gc+T463yvsZ
z5PjUlfR1J1W4dOuYBwLE6zyqgpY9ItY2kL3YWQjUV/OLLDluYSxuLpJHR1Lo496usZVh84OOqcz
7hV/hY4dTBNTyWvonieF7c19MgU2+e2Fhgiknle+iKFGkkbSpY6UQFmsqljYbKCeYYD1VFV0ysdK
tUU00Ks1r6QZEUE23sN7f0OLTUFbURXI4kFLPLHcc41xxstx7RfbAWqpqimZhqVaiGSFmXm1ASKp
IvtcbX9Cxxqzu50oiKWdmPMqqLlifcBfF/gbM7fQqjwYaGeKSGVPlxSo0ci/tI4DD/kYEVPDLPK1
9MUMbyyNYXNkQMxsASbDYC+Oqcz7hV/hY6pzPuFX+FgPVUVXTIx0q1RTTQqzWvpBkRQWsCbDeww1
UtNO1LG2l6kQyGnRrqNLzBeGrXdBYsDd1/SHoWGnilnla+mKGNpZG0gs2lEBY2UFjYbKCTsMPHIr
JJGzI6OpV0dDpZHU2KsrAqykAgix3wscaNI7nSiIpZ2Y+xVW5Y/MBjV8DZnb6HP4L4aKVHikQ2eO
RSjofcyMAyn5iMBVBZmIVVUXZmOwAA3JJ2AG5OOHVU89NIV1BKiKSFypuA2mRVOm4Iva1wfd6eLT
UFbURXI4kFLPLHcc41xoy3HtF9sdU5n3Cr/Cw0cqPFInyo5FKOt9/WRgGG2+45sAAEkmwA3JJ5gB
7ScdU5n3Cr/Cx1TmfcKv8LHEqaGspo7heJPSzwpqPMuqRFW5sbC99jhlo6WoqmQanWnhkmKrzXYI
psL+/HU+Z9yqPw8A1dFV0oJsDUU8sKk2vYNIigm3sH57JvoEH7uHhenzQFJWiZ+BTFBpbSzbVhcq
OfZC1uZb7YBtHXUNQG0PpKyRPupZNaiWnqI/1K6/snely921mlqcwjD2sXjOVVrxOR7C8TI9vZfa
+KD6yH2Wp/oZfRsQGip1acnYconPFm923GkZUvvp0g74pMyUHXRT8GT3cCrsLt+zOkSpvb41/aR6
IamaOP4RnhE9VUvzwq66+TozdHHEm0hW3EcM7eroCmERV0kIfQatIo+Gd7cRIzKJmj9vyBIRzRk2
GF6Nmkh42XV6g6oi6aomuLM8D3HEhb1WG9hKqOtJFINLxivR19zpSzqw/wCCMQTVsdTItRK0SCmS
J2DKmv1uLNCLWHsJN/Zj+y5t/wDRSfz2Kakooa2N4a1aljUxwImhYJ4rLwqiY6ryg7gCwO+My+mr
940Poyz/AM37vqsZ39c5r9vqMQ561OlTm+ahOTGTmjE6PLAgPykhEC8afRZ5nIjLKvDMfG+EQF1X
5PySk4Fv0LGDi6fn4vE/14qcy5PHDnuUIxl4N/jVjTilAPWZ4aiMOadHJaKpRo1k08Rpcr+saH7T
Fim+rIftFV6Xr6MoKiGrYIZE1r8dmscL3X2+pI1vcd8dJR91XxYrMtzWnp4s1pouJTVMIs2gnSJ4
dWqROFKUSpi1tG4kTm16UoY5BpkjzKlR1POrpVRqy/8ADAjEFJQNAIZKCKobiwiRuI1RVRnckbaY
k2/X78dJSd1XxYFHXPAYRKs1o4FjbWgYD1rnb1ztjNfokH8VsOoqYLBmA/qkHsP7OI8oz6ClqqXM
DyYOIQtpX2jWaO5jeORrJsisjsr3sDatoI78BGWSlJNzyeZFkQXJZjwtTQFmOp2iL/3vzuTfQIP3
cVDplTlJKiVlblNCLq0jEHepvzG/NfDU9Yy8pqap6uSNDqWDVFDCsWsbO+mEM7L6t20LqCa2WpgY
NEaqriVl3VuS5HUUpZTzFWaEsrDYg3G2KD6yH2Wp9OW0zIXiE/KJxp1LwqUcciTYgRyMiwnVsTIq
c7DASJrVFZV08cVudRA/K2k5wdIMCRm295V9hvh9CjTmmWiSJZLfFzSxCWHWRrAeCfRcjVpdLi9s
FWVkYGzI4KsrDYqyndWB2IO4OxxnVtrZNmFrbf8AopfRBl9LJTLDTBljd6cSTaWd30szMUIXXpW0
YIVVFzuWpqiU3knOYTSEAKC8lNUO5AGw9YnYbD2Yo4KeohpzTTvMxmDkMGjKWGgH333xNN8IUT8K
J5NOmcatCltN9G17Wv6K6joouPUzVp4cQZE1cOto5X9aRkQWRGbdhzWG9hjql+9UH81ihrK3L2gp
oRVcSUz0j6eJR1ESerFO7m7uo2U89ztjO/rnNft9Rj8jvodJ92Qej8pP9mn/AIVbjK/rGh+0xYpv
qyH7RVemo+mJ99U/oqfqio+2Zfg/9Qn7zxT1OXULVMKZdFCziamjtKtTVuVtNNG2yyIb20+tz3vb
ql+80P8ANejNfokH8VsORlM1i7EfHUnMSf8A3GIMyziNcvo8vcVZ4s0BaR4fXTo5HWOJGAeWSQr6
q6QDq1LW1kJvTXSCma1tUMCBNfvtK+uVbgEI6qdx+dyb6BB+7iaH4HjbhSyR6uWsL6GK3tyU2vbm
vh6WFIcuhlBWUwF2qHRrgpx2I0KRzmONJP8AWBdcZR+1Xfdddig+sh9lqfTmOauu3qUEDe0/Jnqv
Z8n+y2INiQ4I9UYoxQU8b0dJA3rNUQxsaiZ/jfVdgdKxxQ6T7y+IqDNIljlpZZlh0ypNrp3bjISU
JAKvJJGF/QRPfiuUD4qrYV8P7NTdpRzADTUidR/oCkm5OM5VAWZsnrwoXcsTRy2AA5yfYBz+inzC
GShjiqVZ4455Zll0h2RSwSnkQcQLxEs59Rl1aWuop6dypenbMYXKG6FoqaoRip2ut12NhcYopqAU
5eoqXik5RG0g0rEXGkLJHY3HvOJIiMuUSxvGWSlk1AOpUldVSy6hfbUrC/OpG3or6qkmeCoirfi5
U2ZdddRxtb9aMy/qOOuKztjw4y+lq8yqZ6eTlfEikYFW0UVRIt9vY6qw+cYzv65zX7fUY/I76HSf
dkHo/KT/AGaf+DW4yv6xoftMWKb6sh+0VXpqPpiffVP6Kn6oqPtmX4P/AFCfvPFNBQV89LC2Wwyt
HE1lMhqqxC/NzlUQf/EY64rO2P8A89Ga/RIP4rYcDN6ywdgPXHvPzYpc1hmmapy1tGaU0cjLFJp0
LPLLTqeGzJ8TWRsQeDBJLbnP57JvoEH7uKv6VUfxW9GUftV33XXYipq4ziOGbjrwHVG16Hj3LI+2
lztbnx0mY94i/l8R1lE9WZWrI4Dx5UdNDRTOdliQ3vGN7+/GX07DTIYOU1GrYiap+PkDbDotQiF9
wsYvviYQUeXmASyCEutQXMOs8MsVqApYpbUQACeYAYTL66CjgWaGYwtAJldp4gJNHxk0gI4KytYC
91G+KDNFX14JWo5mA/wpgZIi5tssckbqpJA1T252GKegqpo0zOnjWnaKSycsRF0pNCD6sjNGvx8a
+sHDtw1iZMGo4VSitJxDSx1Gmm57sgGkypG2/qJMugHTFw1ChTGhh5WsAjoMvjtt6umFniQrwqWO
25JQMqGOMlyBijd2LO61zOx52ZqScsxt7Sd8QQ1xnC08hlTgOqHUy6Dq1I9xb9WOkzHvEX8vimqq
FqoyS1q07CeVHXQaeol2CxIdWqJd7819sZl9NX7xofRln/m/d9VjO/rnNft9RiHIJKhKbNssCcl4
nNItOrRwuF+U0XJ24E2i7xMBNZl0q3C+D1069PKOV0nAte3E6bjaP71uDxbf4Wr1cVOVLURz57my
sJuCd4kmQxGXnWSOGCLWtMzANJUuZVj08QR5X9Y0P2mLENXQ8l4SUUcB40zRtrWWdzYCN9rSLvf3
4/y/vT/gYpvhDk/9b43C4Epk6Dha9V0S3TJbnvvzWw2X0fD5RPVsU4rFE+JzSOd7sFa3qRtbbc2G
P8v70/4GKvMMzqaefNqqLh01NCb+qu/Bh1hJXR5tD1U5RI1VIwF1KOJQSSMXkkzKld2POzvVRszH
52YknEFXQ8l4UdBFTtxpmjbiJUVUhsBG/q6ZU3vz32x/l/en/AwKyt5LwTKkPxM5kbW4Yj1TGm3q
He/u2xmv0SH+K2JP9x/3jiXKasg0Wcx8nKP8jlIVhGPmE6NJA36btCD8kYq8vfVpie9O7c8tM/rQ
SX2BOg6ZLbCVXX2fnQkdbVxoosqJUTKqj3BQ4AH6vSJIneKRb6XjYo63BU2ZSCLgkGx5iRjrCt71
P48dYVvep/HjRPU1Eyg6gss0ki35r2diL2J3+fGnl1Zptp08pmtbmtbXa1tregSRu0bruroxVlPz
MtiP+MaJqupmTY6JZ5ZFuOY6WYjb2ejQuZ5gqfoLW1IXsiS2C7EszG7MxuzH3kncn5zgSRSPFIL2
eNmRxcWNmUgi42PzY6wre9T+PHWFb3qfx4Cz1NRMoNwJZpJADzXAdjY29uGgE0ogY6mhEjiJm23a
O+gn1V3I/uj3D0CSKR4pFvpeNiji4sbMpBFwSD8xthndizuxZmYkszMbszE7lidyTuTvgOjFWU3V
lJDKfeCNwfnGLfDObW5rfCNZa36uNbDSSMzu5uzuSzMfezG5J+c4DKSCDcEbEEcxB9hGOsK3vU/j
x1hW96n8eF5RUTT6L6eNK8mnVbVp1sbXsL257D3Y0Q1dTCm50RTyxrc850qwG/tx/b63vU/jwZJG
Z3b5TuSzNbbdjcnbbfFxsRuCPYcdYVvep/HjrCt71P48aJ6qomS99Ms0ki399nYi+/PgmCaWEsLM
YpHjJHuOgi49AZSVZSCrA2II3BBG4I9hxrnlkme1tcrtI1hzDUxJt835wHY2IO4BG3vB2I94PPjo
aPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4Md
DR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/Bj
oaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4M
dDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/BjoaPudP4MdDR9zp/B
joaPudP4MdDR9zp/BjoaPudP4MaTHAu97xQRRN7R8pFBtvzc3N7v+3P/xAAoEAEBAAICAgAFBAMB
AAAAAAABEQAhMUEQUSAwYaHwUHGBkUCAscH/2gAIAQEAAT8h/wBcToK0SATfB4ROkX6Px48ePHjx
48ePHjx48ePHjx48ePHjx48ePHjx48ePHjx48T6MLBEJcgXzQIqxl128O56UfXx9FJ0XS9LWtcF1
c+tCoPj7a1PETYK+bDR1mhgsh8BtMC3PDQLrYXObRzz4dHWYGCWngCPeCKH6U5dGETQW9H7b/bGt
NEhShQpshTZrKbGBAz795lSgL5+/dkrNsubqCaGQcM5B1sSRwkwZa59VCerU/tNFI4gFLi0TXgTg
AmAgrwbQ5XpC+s+hW3r/AG/8s0OzZ6OsAjExHhxF/wABiDyuAFAArhoAGqQDlDGgBq8j0oLdrNIu
thcnj6jcgZ8AEioAFQ8OAmcepIBVCABV0efv0Q+FUQUJSTaCBpwd/UBmGVtBgXR4zAhGezhMMWiw
dafn4X6KLL7uId5O2cySiQhKg4pfbDHDXEq5UGjeCilCL8H5xzIFIYppimqjFAzoBRVZbrwJRixq
gZBP9ko3nFw0/OgUcctpUzvEetN0IY90Lozt2iWa7mTTUXuYq3yQBpAuB+hG/FNcLDhTSqndsEHx
z+18egHgcRDnPN2HuYVOAEuVOYpx1XRd5qfPAaVKvi5fw46hnEeQZTKFF22HTwEWnuT4mZBUvZLB
jsv1SSKVhFKacPzlV2ZI10aReBy4DshTwkFRKzep4JfRo2tQ/qYNUS09kj8tQZAwXcmW7yqOCIPn
YReA6R3ECEIHZdZExXyLQJtdlo2bUFWIT3asEZlD8H4mQiKs2ohYvk6/x0qClynq2PKAWq39JsLK
lcFqtIzkyKhJHBICY1jVU2EjJx/Hjc8AQKzFsk5jIFAyUPDDVBgaAGHgiJhTdbRgh3dATSOnXTQt
REFrrBoPveKlqJtUdte3MaY5hv5khHq7s4AUyh+J/Db42Dri6+Ruobv5+U9sEA3+ofVjzWggMJC8
e+f7FP7Hkki0qc6Q7rZ7x5LjpPaJJNepzEkVwifeIMgAV+dgJDf9FvwNksrzhQy5cbXMjR01Pgb/
AIEwQsd3KooOzYslaZmsvaqGBTcA47Dq3jDqiOleg0gadbVQIEZdsZBwLs7hEdQoUgCvgpe06WXA
aK8Y+8ZmEmYmZ4gYWZzuAJ9h41UJqd4c4jJ0soEuKN0uNesaAis220Zaa5fCwqS8FNqfdHD4oBp1
G9VkfzH+n140V0Fno+Quobv5+U9sPhNBuIVuV9YKk5fNJENghqAg/aYpyCKSM8iMnmB/g4E25iUv
NNSbxYOjdTwvEYK12oGMOkODaOYCc94NSJUC6lwCeTJDaZdPWIFqsWAKsqwbBAis/YSomlBEL75+
ZMUt4HT1H8psM46jvK6ItzhxT5AJQmQ2uZAlT/IVomAVqgFdBile922g9LANt3wvpd/18IMBFCjs
ieOf2vj0FkeWEeNHONDMzTdtJXHRpqaI8aML+jKTMUCmiofiOvWSzz0p1kFYmq4L+dHf/wBT7Oi9
V0PdZld76S0wWrt8ksHlAAq5M9XAP8khoAG3PWmiyGp0UFhwrgvSXrWv8NqEj0KnitQWx2u2K3C6
IsmF6Dd3wciYISDCw+Z/I8MFim4AYqqqqtV2q8q9r4+ivEsIxJFY0p527TEbD4iCSAILEWLi90dl
fP8AxkSak8PavQuJWLilQxTELiog7Er1tSnWfn9bP6c0veaDeSGXskxBfmjPKyjtFzmhS9TYSGDt
I6fO3bqpK89iGhILFOHItlsIsJLWpat4M5ZUF24sSSVFpcQBjxYxKtWUKVcAR4onh4F0gmfSb9mu
h9JM0MWZeFGMBRYBhgHPqSgRQCI0dnnbt/FEzgf1cqxgExQAUoD1bUq8+PsHLqLAC2IApgBxiIRQ
IRBoibEdibHzt2lgQE8IgZYIIoL7zdP5Ndqum40vh/YEn1MEAQREpmk2OZs6VFZUKzn5jjiEDOrD
Kugg0k/SGLFixYsWLFixYsWLFixYsWLFixYsWLFixYsWLFixYsWLFiCFhshCCv5ltIko/wBc/wD/
2gAMAwEAAgADAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAABAAAAAA
IIIAJBIAAAJIAIBAAAAIAAAAAAJIIBJBIAIAIBBIAJIJIJAAAAAAIIIAJIBAJAIABIAABIAJAAAA
AAIBIABJABBIIAJIAABIAAAAAAAAIBIJBBABAAIBJBAJJJAJAAAAAAABAIBIIAAIBIIAJBIBIIAA
AAABJJJJJJJJJJJJJJJJJJJJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAA
AAAAAAAAAKD/2gAIAQMBAT8QDx//xAAUEQEAAAAAAAAAAAAAAAAAAACg/9oACAECAQE/EA8f/8QA
JhABAQACAgEEAgMAAwAAAAAAAREAIRAxQSAwUWGB8FBxgJGx0f/aAAgBAQABPxD/ADiFKcmohACU
F/EDyRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIklz2pVAKse0v3YDArtpEpAiOiGj
xF2Zh9J0HtkpuwTGs2XVDqwmXlbkJLcPSPV4ptQnJlF9qkIoCbAIsxZvDDGj1eIbEBiu3ZaRDVpi
6Rwy9JisW0enhr6woHiPRypzeMshSTSUs+oKQoOziLF/KdW1i+mkMhlUHwCiC3QUDiNF0ZCwS9da
QRJ8fcPNScb6XlGgU1il12Ypg8qN4nS2x08bfWO5uWqnwqfH0FBeD/W/YjAMBQbrUisdiGcCcL2n
2mIVQE2AS4kKgG1YB8uFWw+qtFeqBEFP+SFsWqJ5QCoZPvgsV2dQ83vF4lAGOlIJMXqm6iijwXZu
l7YyB2LxpD3f3/xw0dm3S4JbsISKBes/MK9NxDLI7AnktqhHchfQroKgFVADtXQfnNsY0sJtjWW0
K6XDtKRG7tp7gQgE9aD24aAMGNgN9g5dmEojGjR2mFskmG1Bs81cIgbNeIm1sNOMv42stbQMgSk5
ebbXxRgLYBbnv+PD63f9+g+QV8gqensPPfNPS5YpKJgoUmEYoBoZGSmqeIoD6Q+/07yYa84kIixS
IbbfTB+mFj5iPwmPewoVJSwA8TOUzlCTpS6mFUIr1UyhcaQAxUqgzUZ02oN6DQEDYSSMdiH9mAGw
4ohuragVe3eSGab2gRBwAvY0QlSnKL4BAp9z9/8AHGQIxkjb2BBglw2AkXyk/FDeE25DeLHVWyu3
Tm6Cb2El5A1UXP5elCtfWEiGxhRShiVBKhFtEowkMeLteTvdwgY4ihTQaFHiieOG8lkIJ9tDFGEN
4tRPRLpPBEBoingCyLKAACwRjFefxKdEYEOAB0AXuJS4USZztoao1a4KYlfghtZCTcVl4+INlWKJ
dKGM6oAPYKHbxuW1RbVJo6aaabNey+/lm4ZDdtF5uhBwM5ywiFR0CsSnwCroF1wKR2gYFrYoEFhF
BgEsQdYvDY4G2CbDkwTRoZCSzIdumh9z9/8AHDcDk0iIgjcC+ioPRZ1JB046T0rvi60TezQETpGB
wdjHa3q7LnhkKoCGI5VQp/RMswHs1JEYDlDusgHWmc3KKUIIIDlM7WW2zsLKVlftB9uzRlor6gP0
YfYtnQasFYP8aC7Ab2NgGAAAIAA+AIG99fObIxBnISn9WiRRM5bsn4Nc0V+BEtKOENQMKhhBHoQ4
O0Q0piFQqXQCKroAK10b9l9/LNwzlYxwom0giSaqgUwjCYkYhR+EROxHhRjsQwgrUiPZW6AFV13l
D5mr71aGcfet+/8Aj6CPhOriObK3t8CVLCoCFtWuFFRNCwwCAnEkgWNG/fYHnLcR5Q5g9YiqCLEC
IEghDL3ETDf8CC4DlCPwvZKA0ECZJT3f88T9p0QciEacvLPKm+Ea4uHZmwh7G+QQBt/rw6rKVEpG
uCpmdsp01YC/H6T8D5ABPqGQdE//AFuCAMJWaGLPs0KMXDj84UjtKGmd9J78iypecaiQ4fZkAtP/
ANimv1VgKqfSxPo4QdRLy+w/r4y+V6Y3ZVslvqXiCUK1YRlAXgGsQ/79Tqet2GA4fZkBehChDgbI
wIrkFVv3SGWQ9AvQukw6n1BaBut9fu6t94HirtwJ3RWVcRM5ZQKgqhVVVVVvDeaT3MWu/bFDnGPG
RnoI7GqEBKhK1IEhtmrLYq7ujhTPVjEvRY2QIopUiqTUxuFrtDiDKDES+FCH2Aj2IJsxM8JsfcvN
1LVo4YsheADzAEAAXRgb1AIEzMPHupB4x4/iGr/GPV1vFBIDYGI1gLIhU3D84ZDy8vxtDL8MFsxb
rmcgu/x1t1u3/QJMDJMyJiJJlOvA8Y5Pi+iW5KbYEAAsuhbNoieEIIPOPH+xM+W/+FZ6Kk1SSYQn
aS8U3N830S8sKhEACf4gGS8DhAAIiDznxgVyr2pEyJmIISA6DCgULQ4bBd533h1OpXxIeScgg4SA
zjSADXe7MBV9tisV1EtlEUVUk/iLdu3bt27du3bt27du3bt27du3bt27du3bt27du3bt27du2M3S
SCOCEhSRJ/nL/9k='''

import os, sys
from pathlib import Path
import argparse
import re
from typing import *
import gpxpy
import gpxpy.gpx as pgpx
import uuid
from lxml import etree

process_all_files = False
def msfs_name_type(arg_value, pat=re.compile(r"^[a-z0-9]{,10}$")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("invalid value, valid are max. 10 lowercase letters and numbers (see sdk)")
    return arg_value

parser = argparse.ArgumentParser(
    description='''Read gpx-files and show them as POI in MSFS2020 during flight.
                This script creates a MSFS2020 project structure ready to compile
                with ms flight simulator''')
parser.add_argument('inputfile', nargs="?", help="a gpx file or pattern like *.gpx")
parser.add_argument('-s', '--sceneryname', help='Name for this scenery',type=msfs_name_type, default=__default_scenery_name__)
parser.add_argument('-o', '--outputpath', help='Name for output directory')
parser.add_argument('-c', '--creator', help='creators name',type=msfs_name_type, default=__creator__)
parser.add_argument('-m', '--manufacturer', help='manufacturer name',type=msfs_name_type,default=__manufacturer__)
parser.add_argument('-z', '--offset', help='add this offset to each POI', type=int, default=0)
parser.add_argument('--mindistance', help='minimum distance between each POI', type=int)
parser.add_argument('--cleanup', help='Clean outputpath and delete all files DANGER!', action='store_true')
parser.add_argument("-v", "--verbose", dest="logLevel", type=str.upper, default="INFO",
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help="Set the logging level")

args = parser.parse_args()

try:
    from loguru import logger as log

    logger_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<light-blue>{file}:<bold>{line: >4}</bold></light-blue> <cyan>{name}</cyan>:<cyan>{function}</cyan> | "
        "<level>{message}</level>")
    log.remove()
    log.add(sys.stderr, level=args.logLevel, format=logger_format)
    log.add(__file__ + ".log", rotation="1 day", level=args.logLevel, format=logger_format)
    log.debug("using  loguru")
except:
    import logging

    log = logging.getLogger(__name__)
    log.setLevel(logging.getLevelName(args.logLevel))
    fmt = "%(asctime)s %(name)s %(levelname)s %(message)s"
    logformatter = logging.Formatter(fmt)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter(fmt))
    floghandler = logging.FileHandler(f"{__name__}.log", mode='w')
    floghandler.setFormatter(logging.Formatter(fmt))
    log.addHandler(floghandler)
    log.addHandler(stdout_handler)
    log.debug("using native log method")
log.info(f"Welcome to {Path(__file__).name} version {__version__}")
log.debug(f"command line parameters: {args}")


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    taken from https://stackoverflow.com/a/3041990
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError(f"invalid default answer: '{default}'")

    while True:
        sys.stdout.write("\n"+question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def add_node(tree, element, text):
    child = etree.Element(element)
    child.text = text
    tree.append(child)
    return child



def escape(text):
    """
        :param text: a plain text message
        :return: the message escaped
        taken and adjusted from https://stackoverflow.com/a/25875504
    """

    conv = {
        '&': r'',
        '%': r'',
        '$': r'',
        '#': r'',
        '_': r'-',
        '{': r'',
        '}': r'',
        '~': r'',
        '^': r'',
        '\\': r'',
        '<': r'(',
        '>': r')',
        '\n': r'',
        '\r': r'',
        '"': r''
    }

    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key=lambda item: - len(item))))
    try:
        res = regex.sub(lambda match: conv[match.group()], text)
    except Exception as ex:
        log.warning(text + f"reason: {ex}")
        res = text
    return res



if args.outputpath:
    outputpath = Path(args.outputpath)
else:
    currentpath = Path.cwd()
    outputpath = currentpath.joinpath("msfs_project_dir")
log.info(f"Using outputpath {outputpath}")

if outputpath.is_dir():
    log.warning("Outputpath already exists")
    if args.cleanup and query_yes_no(
            f"Do you really want to delete {outputpath} and all files within? You can not undo this action!",
            default='no'):

        import shutil
        try:
            shutil.rmtree(outputpath)
            log.warning(f"outputpath {outputpath} deleted!")
        except Exception as ex:
            log.error(f"Could not remove files, reason: {ex}")
            exit(1)
    else:
        log.error(
            f"OutputPath  {outputpath} exists, exiting...  You can provide --cleanup to clean up, but be careful!")
        exit(1)

package_definitions_dir = outputpath.joinpath('PackageDefinitions')
log.info(f"using {package_definitions_dir} for PackageDefinitions")
packages_dir = outputpath.joinpath('Packages')
log.info(f"using {packages_dir} for Packages")
package_metadata_dir = outputpath.joinpath('PackagesMetadata')
log.info(f"using {package_metadata_dir} for PackagesMetadata")
package_source_dir = outputpath.joinpath('PackageSources')
log.info(f"using {package_source_dir} for PackageSources")
package_definitions_dir.mkdir(parents=True, exist_ok=True)
packages_dir.mkdir(parents=True, exist_ok=True)
package_metadata_dir.mkdir(parents=True, exist_ok=True)
package_source_dir.mkdir(parents=True, exist_ok=True)


def gpx_part_info(gpx_part: Union[pgpx.GPX, pgpx.GPXTrack, pgpx.GPXTrackSegment]):
    """
    gpx_part may be a track or segment.
    # taken and modified from https://github.com/tkrajina/gpxpy/blob/dev/gpxinfo
    """
    length_2d = gpx_part.length_2d()
    length_3d = gpx_part.length_3d()

    points_no = len(list(gpx_part.walk(only_points=True)))
    result = 0

    for track in gpx_part.tracks:
        for segment in track.segments:
            result += len(segment.points)
    result += len(gpx_part.waypoints)
    result += len(gpx_part.routes)

    bounds = gpx_part.get_bounds()
    distances = 0
    avg_dist = None
    if points_no > 0:
        distances: List[float] = []
        previous_point = None
        for point in gpx_part.walk(only_points=True):
            if previous_point:
                distance = point.distance_2d(previous_point)
                distances.append(distance)
            previous_point = point
        avg_dist = (sum(distances) / len(list(gpx_part.walk())))
    return points_no, length_2d, length_3d, avg_dist, bounds


def create_package_definition(name: Path, title='Test', creator=__creator__, Manufacturer=__manufacturer__):
    # create the xml-File in PackageDefinitions and the directory with the same name (without .xml)
    #defname=f'{name.name.replace(".","")}'
    defname="".join(x for x in name.name if (x.isalnum() or x in "-"))
    #defname = "".join(x for x in name.name if (x.isalnum()))
    output_filename = package_definitions_dir.joinpath(defname, 'ContentInfo')
    log.debug(f"outputdir contentinfo: {output_filename}")
    output_filename.mkdir(parents=True, exist_ok=True)
    asset_dir = package_source_dir.joinpath('Scenery', defname).relative_to(outputpath)
    output_dir = str(package_source_dir.joinpath('Scenery', defname).relative_to(package_source_dir))
    # create default thumbnail from internal version:
    # https://stackoverflow.com/questions/27601972/embedding-binary-data-in-a-script-efficiently
    thumbnailfile = output_filename.joinpath('Thumbnail.jpg')
    import base64
    b = base64.b64decode(Thumbnail_jpg)
    with thumbnailfile.open('wb') as f:
        f.write(b)
        f.close()

    project = etree.Element('AssetPackage', Version='0.1.0')
    add_node(project, "OutputDirectory", ".")
    add_node(project, "TemporaryOutputDirectory", "_PackageInt")
    ItemSettings = etree.SubElement(project, "ItemSettings")
    add_node(ItemSettings, "ContentType", "SCENERY")
    add_node(ItemSettings, "Title", title)
    add_node(ItemSettings, "Manufacturer", Manufacturer)
    add_node(ItemSettings, "Creator", creator)

    Flags = etree.SubElement(project, "Flags")
    add_node(Flags, "VisibleInStore", "false")
    add_node(Flags, "CanBeReferenced", "false")

    AssetGroups = etree.SubElement(project, "AssetGroups")
    AssetGroup = etree.SubElement(AssetGroups, "AssetGroup", Name="ContentInfo")
    add_node(AssetGroup, "Type", "ContentInfo")
    add_node(etree.SubElement(AssetGroup, "Flags"), "FSXCompatibility", "false")
    add_node(AssetGroup, 'AssetDir',
             str(package_definitions_dir.joinpath(defname, "ContentInfo").relative_to(outputpath)))
    add_node(AssetGroup, 'OutputDir', str(package_definitions_dir.joinpath(defname).relative_to(outputpath)))
    #AssetGroup.insert(0, etree.Comment(' '))  # 0 is the index where comment is inserted
    AssetGroupPOI = etree.SubElement(AssetGroups, "AssetGroup", Name="POI")
    add_node(AssetGroupPOI, "Type", "BGL")
    add_node(etree.SubElement(AssetGroupPOI, "Flags"), "FSXCompatibility", "false")
    add_node(AssetGroupPOI, 'AssetDir', str(asset_dir))
    add_node(AssetGroupPOI, 'OutputDir',str(output_dir))

    s = (b'<?xml version="1.0" encoding="UTF-8"?>' +
         etree.tostring(project, pretty_print=True, encoding="UTF-8", xml_declaration=False))
    output_filename = package_definitions_dir.joinpath(defname+'.xml')
    output_filename.parent.mkdir(parents=True, exist_ok=True)
    log.info(f"creating package definition {output_filename}")
    with output_filename.open('wb') as f:
        f.write(s)
        f.close()
    log.info(f"created {output_filename}")
    return defname

# Parsing an existing file:
# -------------------------
all_files = []
if not args.inputfile is None:
    # user provided a name, check if a filename fits:
    inputfile = Path(args.inputfile)
    if not (inputfile.is_file()):
        log.info(f"Try to find all inputfiles in path {inputfile.parent}")
        basename = inputfile.name.removesuffix("".join(inputfile.suffixes))
        all_files = list(Path(inputfile).parent.glob(basename + ".gpx"))
    else:
        all_files = [inputfile]
else:
    # user did not provided a name or pattern:
    log.error("missing inputfile[s]!")
    parser.print_help()
    exit(1)

log.info(f"I found these inputfile[s]:{all_files}")

def handle_gpx(input, title=__default_scenery_name__, creator=__creator__, Manufacturer=__manufacturer__):
    log.debug(f"try to open {input}")
    gpx_file = open(input, 'r')
    try:
        gpx = gpxpy.parse(gpx_file)
    except Exception as ex:
        log.error(f"reason: {ex}")
        log.error(f"Is the provided file {input} a valid gpx file?")
        exit(1)
    if gpx.copyright_author:
        log.info(f"{gpx.copyright_author}")
    if gpx.creator:
        log.info(f"GPX-File Creator: {gpx.creator}")
    if gpx.description:
        log.info(f"GPX Description:{escape(gpx.description)}")
    points, len2d, len3d, avg_dist, bounds = gpx_part_info(gpx)
    log.info(f"GPX file contains {len(gpx.waypoints)} Waypoints, {len(gpx.routes)} Routes and {len(gpx.tracks)} Tracks")
    if bounds:
        log.info(
            f'This gpxfile covers {bounds.max_latitude :.1f}° ...{bounds.min_latitude :.1f}° North to South  and {bounds.max_longitude :.1f}°...{bounds.min_longitude:.0f}° East to West')
    if len2d:
        log.info(f'Length 2D: {len2d / 1000.:.1f}km 3D: {len3d / 1000.:.1f}km')
    log.info(f'Points: {points}')
    if avg_dist:
        log.info(f'Avg distance between points: {avg_dist:.0f}m')
    if args.mindistance:
        gpx.simplify(args.mindistance)
        log.info(f"adjusted no of points with mindistance={args.mindistance}m to {gpx.get_points_no()} points")

    if gpx.get_points_no() > 1000:
        log.warning(
            f"The file contains too many points or points that are too close together. This affects the frame rate in MSFS. Try to correct this in advance, e.g. using option --mindistance 1000 or with GPSbabel https://www.gpsbabel.org/")

    i = 0
    project = etree.Element('FSData', version='9.0')

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                i = i + 1
                info = ', '.join(filter(None, [str(i), point.name, point.description]))
                info = escape(info)
                POI = etree.SubElement(project, "LandmarkLocation", instanceId=f"{{{str(uuid.uuid4()).upper()}}}",
                                       type="POI", name=f"{info}", lat=f"{point.latitude}", lon=f"{point.longitude}",
                                       alt=f"{point.elevation if point.elevation else 0}", offset=f"{args.offset}")
    for point in gpx.waypoints:
        i = i + 1
        info = ', '.join(filter(None, [str(i), point.name, point.description]))
        info = escape(info)
        POI = etree.SubElement(project, "LandmarkLocation", instanceId=f"{{{str(uuid.uuid4()).upper()}}}",
                               type="POI", name=f"{info}", lat=f"{point.latitude}", lon=f"{point.longitude}",
                               alt=f"{point.elevation if point.elevation else 0}", offset=f"{args.offset}")

    for route in gpx.routes:
        for point in route.points:
            i = i + 1
            info = ', '.join(filter(None, [str(i), route.name, route.description]))
            info = escape(info)
            POI = etree.SubElement(project, "LandmarkLocation", instanceId=f"{{{str(uuid.uuid4()).upper()}}}",
                                   type="POI", name=f"{info}", lat=f"{point.latitude}", lon=f"{point.longitude}",
                                   alt=f"{point.elevation if point.elevation else 0}", offset=f"{args.offset}")


    s = (b'<?xml version="1.0"?>' +
         etree.tostring(project, pretty_print=True, encoding="UTF-8", xml_declaration=False))

    #defname = input.name.replace(".", "")
    # create a name like aaa-bbb-ccc...-xxx.xml only lowercase and numbers
    defname = "".join(x for x in input.name if (x.isalnum() or x in "-"))

    pname = f"{Manufacturer.lower()}-{creator.lower()}-{title.lower()}-{defname}"
    output_filename = package_source_dir.joinpath("Scenery", pname,pname + ".xml")
    output_filename.parent.mkdir(parents=True, exist_ok=True)
    log.info(f"creating scenery file {output_filename}")
    with output_filename.open('wb') as f:
        f.write(s)
        f.close()
    return pname


def create_main_xml(packages, title=__default_scenery_name__, creator=__creator__, Manufacturer=__manufacturer__):
    project = etree.Element('Project', Version='2', Name=creator, FolderName='Packages',
                            MetadataFolderName='PackageMetadata')
    add_node(project, "OutputDirectory", ".")
    add_node(project, "TemporaryOutputDirectory", "_PackageInt")
    packagestree = etree.SubElement(project, "Packages")
    for pack in packages:
        add_node(packagestree, "Package", "PackageDefinitions\\" + escape(pack))

    s = (b'<?xml version="1.0" encoding="UTF-8"?>' +
         etree.tostring(project, pretty_print=True, encoding="UTF-8", xml_declaration=False))
    output_filename = outputpath.joinpath(f"{title}.xml")
    output_filename.parent.mkdir(parents=True, exist_ok=True)
    with output_filename.open('wb') as f:
        f.write(s)
        f.close()
    log.info(f"scenery package {output_filename} created")
    log.info(f"you can now compile this file with fspackagetool of from within the developer menu inside of msfs")
    log.info(f"all you need is in {outputpath}")

packages = []
for input in all_files:
    pname = handle_gpx(input,title=args.sceneryname,creator=args.creator,Manufacturer=args.manufacturer)
    packages.append(f'{pname}.xml')
    create_package_definition(Path(pname),title=args.sceneryname,creator=args.creator,Manufacturer=args.manufacturer)
create_main_xml(packages,title=args.sceneryname,creator=args.creator,Manufacturer=args.manufacturer)

