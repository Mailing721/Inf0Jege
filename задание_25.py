import fnmatch

def task_13440():
    for i in range(0,10**9,2658):
        if fnmatch.fnmatch(str(i),'85*16?4') and i%2658==0:
            print(i,i//2658)

def task_13429():
    for i in range(0,10**6,83):
        if fnmatch.fnmatch(str(i),"1*578*") and i%83==0:
            print(i,i//83)

def task_13428():
    for i in range(0,10**7,685):
        if fnmatch.fnmatch(str(i),"23*61*5") and i%685==0:
            print(i,i//685)

def task_12741():
    for i in range(0,10**10,1234):
        if fnmatch.fnmatch(str(i),"4*5*6") and fnmatch.fnmatch(str(i),"?74*68") and i%1234==0:
            print(i,i//1234)
            
if __name__ == f"__main__":
    task_13440()
    task_13429()
    task_13428()
    #12932
    task_12741()
