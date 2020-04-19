import asyncio
from stoq import Stoq

loop = asyncio.get_event_loop()
s = Stoq(plugin_dir_list=['plugins'], always_dispatch=['w1','w2','w3'], log_level='DEBUG')
loop.run_until_complete(s.scan(content=b'asyncio'))


loop.run_until_complete(s.scan(content=b'time'))
