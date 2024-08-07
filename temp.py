import concurrent.futures
def reader():
    with open('data.txt','r') as in_file:
        for row in in_file:   
            in_data = in_file.readlines()
            for  i in range(0,len(in_data), 20):
                chunk = in_data[i:i+20]
                yield chunk

def processor(chunk):
    block = []
    block_sum = []
    for j in chunk:
        for a in j:
            a=a.split(",")
            for e in a:
                    e = int(e.replace("\n", ""))
                    block.append(e)
                                
        sb = sum(block)   
    block_sum.append(sb)
    return block_sum[1]

with concurrent.futures.ThreadPoolExecutor() as exe:
    results = []
    results = reader()

    for result in results:
        final = [exe.submit(processor,result) for result in results] 
    
    for f in concurrent.futures.as_completed(final):
        print(f.result()) 