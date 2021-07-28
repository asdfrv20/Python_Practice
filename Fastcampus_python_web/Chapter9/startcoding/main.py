# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈
from unit import item
item.test()

# 3. from 패키지 import * 
# : 여기에서 '*(astolisk)'기호는 "모든"을 뜻하는 기호이다.
# 이러한 방식으로 사용할 경우 "__init__.py" 파일에 'from . import 모듈들이름'을 추가해 주어야 한다. 
from unit import *
character.test()
item.test()
monster.test()

# 4. import 패키지 
# : 이 방식 역시 3. 과 마찬가지로 "__init__.py" 파일에 "from . import 모듈들이름"을 추가해 주어야 한다. 
import unit
unit.character.test()
unit.item.test()
unit.monster.test()

