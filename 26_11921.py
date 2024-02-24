import tkinter.filedialog

def task_11921():
    with open(tkinter.filedialog.askopenfilename()) as file:
        n = int(file.readline())
        p = []
        for i in range(n):
            p.append(int(file.readline()))

        p.sort(reverse=True)
        m = int(file.readline())
        d = []
        for _ in range(m):
            b, c = map(int, file.readline().split())
            d.append((b, c))

        d.sort()
        f, s = 0, m - 1
        a = 0
        o = 10e20
        m_p = 0
        t = True
        for f in range(n):
            while s >= 0 and p[f] <= d[s][0]: 
                if d[s][1] < o:
                    o = d[s][1]

                s -= 1
            
            if t:
                m_p = o
                t = False
            
            a += o
        
        print(f"{a, m_p}")

if __name__ == f"__main__":
    task_11921()
