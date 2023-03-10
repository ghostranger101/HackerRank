if __name__ == '__main__':
    
    def avg(li,leng):
        sum=0
        for i in li:
            sum=sum+i
        print("%.2f"%(sum/3))
    
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    name = input()
    avg(student_marks[name],len(student_marks[name]))

