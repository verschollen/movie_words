from types import SimpleNamespace
from src.utils.keyboards import create_keyboard 

                                 
keys = SimpleNamespace(
    random_connect = ":ghost: random connect",
    settings = ":gear: settings"
)

keyboards = SimpleNamespace(
    main = create_keyboard(keys.random_connect, keys.settings)
    
)


