import hashlib
import os
import requests
import zlib
from PIL import Image
'''part2_list = [
    '125011','150823','155503',
    '140837','130015','123501',
    '141117','169615','132807',
    '121907','144413','131945',
    '140905','162405','165611', #18+9 = 27 totals
    '114709','142011','152813']'''
new_christmas = ['155203'] #+2 new
#edit id list 
#edit save path 
save_path = "E:/t/flower_girl_part2/.temp1"

url_r18 = 'https://dugrqaqinbtcq.cloudfront.net/product/ynnFQcGDLfaUcGhp/assets/hscene_r18_spine/'


for id in new_christmas:
    print(id)
    path_per_id = os.path.join(save_path,id)
    os.makedirs(path_per_id,exist_ok=True)
    #atlas
    md5_name = hashlib.md5(('atlasr18_spine_'+id+'_000').encode()).hexdigest()
    res = requests.get(url_r18+md5_name+'.bin')
    #print('atlasr18_spine_'+id+'_000')
    #print(url_r18+md5_name+'.bin')
    with open(os.path.join(path_per_id,'atlasr18_spine_'+id+'_000.atlas.txt'),'wb') as fp:
        fp.write(zlib.decompress(res.content))
        

    md5_name = hashlib.md5(('spiner18_spine_'+id+'_000').encode()).hexdigest()
    res = requests.get(url_r18+md5_name+'.bin')
    #p/rint(url_r18+md5_name+'.bin')
    with open(os.path.join(path_per_id,'spiner18_spine_'+id+'_000.json'),'wb') as fp:
        fp.write(zlib.decompress(res.content))
    
    #images loop
    for i in range(0,7):
        if i == 0:
            webpname = 'webpr18_spine_'+id+'_000'
            webpsavename = 'r18_spine_'+id+'_000'
        else:
            webpname = 'webpr18_spine_'+id+'_000_'+str(i+1)
            webpsavename = 'r18_spine_'+id+'_000_'+str(i+1)

        md5_name = hashlib.md5((webpname).encode()).hexdigest()
        res = requests.get(url_r18+md5_name+'.bin')
        if res.status_code == 200:
            #print(webpname)
            #print(url_r18+md5_name+'.bin')
            with open(os.path.join(path_per_id,webpsavename+'.png'),'wb') as fp:
                fp.write(zlib.decompress(res.content))
            img = Image.open(os.path.join(path_per_id,webpsavename+'.png'))
            img.save(os.path.join(path_per_id,webpsavename+'.png'),'png')
        else:
            print('not found:'+str(i+1))

    

