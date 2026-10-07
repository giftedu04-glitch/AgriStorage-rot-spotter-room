#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'src'))
from rotspotter.detector import EdgeDetector
from rotspotter.queue_manager import QueueManager
from rotspotter.env import EnvSensor

def main():
    print('AgriSafe Rot-Spotter (Edge/Offline)')
    qm=QueueManager('data/queue.json'); det=EdgeDetector(); env=EnvSensor()
    while True:
        print('\n1) Add crate 2) List 3) Rotate 4) Env 5) Quit')
        c=input('> ').strip()
        if c=='1':
            cid=input('Crate ID: ').strip() or 'crate-1'
            img=input('Image path: ').strip()
            if not os.path.exists(img): 
                print('Image not found'); continue
            res=det.predict(img, env.read())
            crate=qm.add_crate(cid,res['score'],res['source'])
            print(crate)
        elif c=='2': [print(x) for x in qm.list()]
        elif c=='3': print(qm.rotate())
        elif c=='4': print(env.read())
        elif c=='5': break
        else: print('Invalid')

if __name__=='__main__': main()
