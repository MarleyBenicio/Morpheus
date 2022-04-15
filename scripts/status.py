from tqdm import tqdm

import time

def status():
	for i in tqdm(range(100)):
	    time.sleep(0.1)
