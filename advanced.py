
from tkinter import*;
root = Tk();
root.title("Calculator")
nums=[];
entry = Entry(root,width =50,borderwidth =4)
entry.grid(row =0,column =0,columnspan =6,padx=10,pady=10);
present = "";
currans =0;
currentsign="";
def Enter():
    global nums;
    global present,currans,currentsign;
    temp = int(present);
    nums.append(temp);
    print(currans,nums[1],sep="  ");
    entry.delete(0,END);
    if(currentsign == "+"):
        temp = int(currans)+int(nums[1]);
        entry.insert(0,temp);
        print('hello');
    elif(currentsign == "-"):
        entry.insert(0,currans-nums[1]);
    elif(currentsign == "/"):
        entry.insert(0,currans/nums[1]);
    elif(currentsign == "*"):
        entry.insert(0,currans*nums[1]);

    """temp=0;
    for i in nums:
        temp+=i;
    entry.insert(0,temp);
    present=""; """
    nums.clear();
    present ="";

def regClicks(num):
    global present,currans,nums,currentsign;
    if(num =="+"):
        temp = int(present);
        nums.append(temp);
        if(len(nums)==1):
            currans = nums[0];
        else:
            currans = nums[0]+nums[1];
            nums.clear;
            nums.append(currans);        
        present = "";
        temp1 = entry.get();
        entry.delete(0,END);
        entry.insert(0,temp1+"+");
        currentsign ="+";
    elif(num =="-"):
        temp = int(present);
        nums.append(temp);
        if(len(nums)==1):
            currans = nums[0];
        else:
            currans = nums[0]-nums[1];
            nums.clear;
            nums.append(currans);
        present = "";
        temp1 = entry.get();
        entry.delete(0,END);
        entry.insert(0,temp1+"-");
        currentsign ="-";
    elif(num =="/"):
        temp = int(present);
        nums.append(temp);
        if(len(nums)==1):
            currans = nums[0];
        else:
            currans = nums[0]/nums[1];
            nums.clear;
            nums.append(currans);
        present = "";
        temp1 = entry.get();
        entry.delete(0,END);
        entry.insert(0,temp1+"/");
        currentsign = "/";
    elif(num == "*"):
        temp = int(present);
        nums.append(temp);
        if(len(nums)==1):
            currans = nums[0];
        else:
            currans = nums[0]*nums[1];
            nums.clear;
            nums.append(currans);
        present = "";
        temp1 = entry.get();
        entry.delete(0,END);
        entry.insert(0,temp1+"*"); 
        currentsign = "*"; 
    else:
        present = present +num;
        temp =entry.get();
        entry.delete(0,END);
        entry.insert(0,temp+num);
def Clear():
    global present,nums;
    present = "";
    nums.clear;
    entry.delete(0,END);
but1 = Button(root,text ='1',padx =50,pady=20,command = lambda: regClicks("1"));
but2 = Button(root,text ='2',padx =50,pady=20,command = lambda: regClicks("2"));
but3 = Button(root,text ='3',padx =50,pady=20,command = lambda: regClicks("3"));
but4 = Button(root,text ='4',padx =50,pady=20,command = lambda: regClicks("4"));
but5 = Button(root,text ='5',padx =50,pady=20,command = lambda: regClicks("5"));
but6 = Button(root,text ='6',padx =50,pady=20,command = lambda: regClicks("6"));
but7 = Button(root,text ='7',padx =50,pady=20,command = lambda: regClicks("7"));
but8 = Button(root,text ='8',padx =50,pady=20,command = lambda: regClicks("8"));
but9 = Button(root,text ='9',padx =50,pady=20,command = lambda: regClicks("9"));
but0 = Button(root,text ='0',padx =50,pady=20,command = lambda: regClicks("0"));
butEnter = Button(root,text = 'enter',padx =39.5,pady=20,command = Enter);
butPlus =Button(root,text ='+',padx =50,pady=20,command = lambda: regClicks("+"));
butDiv = Button(root,text ='/',padx =50,pady=20,command = lambda: regClicks("/"));
butSub = Button(root,text ='-',padx =50,pady=20,command = lambda: regClicks("-"));
butMul = Button(root,text ='*',padx =50,pady=20,command = lambda: regClicks("*"));
butClear = Button(root, text ="Clear",width = 50,pady=20,command =Clear);

but7.grid(row =1 ,column =1 );
but8.grid(row =1 ,column =2 );
but9.grid(row =1 ,column = 3);
but4.grid(row = 2,column =1 );
but5.grid(row = 2,column = 2);
but6.grid(row = 2,column = 3);
but1.grid(row =3 ,column =1 );
but2.grid(row = 3,column = 2);
but3.grid(row = 3,column = 3);
but0.grid(row = 4,column = 1);
butEnter.grid(row = 4,column = 2);
butPlus.grid(row = 4,column = 3);
butSub.grid(row = 5,column =1);
butMul.grid(row = 5,column =2);
butDiv.grid(row = 5,column =3);
butClear.grid(row =6,column=1,columnspan =3);

root.mainloop();


