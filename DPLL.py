import sys
import copy
""" DPLL ALGORITHM """
def DPLL(sentence):
    components=eval(sentence)
    clauses=extract_clauses(components)
    literals=extract_literals(clauses)
    truth_values=[]

    check_1=1
    
    while check_1==1:
        #pure_symbol_check
        pure_symbol_recursion=1
        while(pure_symbol_recursion==1):
             pure_symbol_recursion=pure_symbols(clauses,literals,truth_values,pure_symbol_recursion)
    
        if(len(clauses)==0):
            truth_values.insert(0,"true")
            while(len(literals)!=0):
                truth_value=literals.pop()+"=true"
                truth_values.append(truth_value)
            return truth_values
            

        
        if(len(clauses)!=0):
            flag=1
            for clause in clauses:
                if (len(clause)==1 or (len(clause)==2 and clause[0]=="not")):
                    flag=0
            if flag==1:
                check_1=0
                break
        
        #unit_clause_check
        unit_clause_recursion=1
        while(unit_clause_recursion==1):
            unit_clause_recursion=unit_clauses(clauses,literals,truth_values,unit_clause_recursion)
    
        if(len(clauses)==0):
            truth_values.insert(0,"true")
            while(len(literals)!=0):
                truth_value=literals.pop()+"=true"
                truth_values.append(truth_value)
            return truth_values       
        else:
            for clause in clauses:
                if(len(clause)==0):
                    del truth_values[:]
                    truth_values.append("false")
                    return truth_values
                    
         
    #splitting rule
    temp_clauses=copy.deepcopy(clauses)
    temp_literals=copy.deepcopy(literals)
    temp_truth_values=copy.deepcopy(truth_values)
    clauses.append(literals[0])
    #case1
    check_1=1
    while check_1==1:
       unit_clause_recursion=1
       while(unit_clause_recursion==1):
           unit_clause_recursion=unit_clauses(clauses,literals,truth_values,unit_clause_recursion)

       if(len(clauses)==0):
           check_1=0
           break

       if(len(clauses)!=0):
            flag=1
            for clause in clauses:
                if (len(clause)==0):
                    flag=0
            if flag==0:
                check_1=0
                break
       
       pure_symbol_recursion=1
       while(pure_symbol_recursion==1):
           pure_symbol_recursion=pure_symbols(clauses,literals,truth_values,pure_symbol_recursion)

       if(len(clauses)==0):
           check_1=0
           break

       if(len(clauses)!=0):
            flag=1
            for clause in clauses:
                if (len(clause)==1 or (len(clause)==2 and clause[0]=="not")):
                    flag=0
            if (flag==1 and len(literals)==0):
                check_1=0
                break
            else:
                clauses.append(literals[0])

    if(len(clauses)==0):
              truth_values.insert(0,"true")
              while(len(literals)!=0):
                  truth_value=literals.pop()+"=true"
                  truth_values.append(truth_value)
              return truth_values           
    else:
        clauses=copy.deepcopy(temp_clauses)
        literals=copy.deepcopy(temp_literals)
        truth_values=copy.deepcopy(temp_truth_values)
        clauses.append(["not",literals[0]])

        #case 2
        check_1=1
        while check_1==1:
            unit_clause_recursion=1
            while(unit_clause_recursion==1):
                unit_clause_recursion=unit_clauses(clauses,literals,truth_values,unit_clause_recursion)

            if(len(clauses)==0):
                      truth_values.insert(0,"true")
                      while(len(literals)!=0):
                          truth_value=literals.pop()+"=true"
                          truth_values.append(truth_value)
                      return truth_values             
            else:
               for clause in clauses:
                   if(len(clause)==0):
                       del truth_values[:]
                       truth_values.append("false")
                       return truth_values
                       

            pure_symbol_recursion=1
            while(pure_symbol_recursion==1):
               pure_symbol_recursion=pure_symbols(clauses,literals,truth_values,pure_symbol_recursion)
            
            if(len(clauses)==0):
                      truth_values.insert(0,"true")
                      while(len(literals)!=0):
                          truth_value=literals.pop()+"=true"
                          truth_values.append(truth_value)
                      return truth_values
                      

            if(len(clauses)!=0):
                flag=1
                for clause in clauses:
                    if (len(clause)==1 or (len(clause)==2 and clause[0]=="not")):
                        flag=0
                if (flag==1 and len(literals)==0):
                   check_1=0
                   break
                else:
                   clauses.append(["not",literals[0]])

        if(len(clauses)==0):
              truth_values.insert(0,"true")
              while(len(literals)!=0):
                  truth_value=literals.pop()+"=true"
                  truth_values.append(truth_value)
              return truth_values
              
        else:
            del truth_values[:]
            truth_values.append("false")
            return truth_values
            
 

""" EXTRACT CLAUSES"""
def extract_clauses(components):
     clauses=[]
     if components[0]=="and":
         for literal in components:
             if literal=="and":
                 continue
             else:
                 clauses.append(literal)
     else:
         clauses.append(components)

     return clauses

""" EXTRACT LITERALS """
def extract_literals(clauses):
    literals=[]
    for clause in clauses:
        if(len(clause)==1):
            if(clause not in literals):
                literals.append(clause)
        elif(len(clause)==2 and clause[0]=="not"):
             if(clause[1] not in literals):
                literals.append(clause[1])
        else:
            for literal in clause:
                if literal=="or":
                    continue
                elif(len(literal)==1):
                    if(literal not in literals):
                        literals.append(literal)
                elif(len(literal)==2 and literal[0]=="not"):
                    if(literal[1] not in literals):
                        literals.append(literal[1])


    return literals

""" PURE SYMBOLS """
def pure_symbols(clauses,literals,truth_values,pure_symbol_recursion):
     delete_literals=[]
     for check_literal in literals:
         positive=0
         negative=0
         for clause in clauses:
             if(clause[0]!="not"):
                for literal in clause:
                    if(len(literal)==1):
                        if check_literal==literal:
                            positive=positive+1
                    elif(len(literal)==2 and literal[0]=="not"):
                        if check_literal==literal[1]:
                            negative=negative+1
             elif(clause[0]=="not"):
                 if check_literal==clause[1]:
                     negative=negative+1
    
    
         if(positive==0 or negative==0): #Pure Symbol found
             if(positive!=0 and negative==0):
                 truth_value=check_literal+"=true"
                 truth_values.append(truth_value)
                 delete_literals.append(check_literal)
                 pure_symbol_delete(clauses,check_literal)
             elif(positive==0 and negative!=0):
                 truth_value=check_literal+"=false"
                 truth_values.append(truth_value)
                 delete_literals.append(check_literal)
                 check_literal=["not",check_literal]
                 pure_symbol_delete(clauses,check_literal)
    
     if(len(delete_literals)==0):
         pure_symbol_recursion=0
     else:
        temp_literals=[]
        for literal in literals:
            flag=1
            for delete_literal in delete_literals:
               if(literal==delete_literal):
                   flag=0
            if flag==1:
               temp_literals.append(literal)
        
        del literals[:]
        for literal in temp_literals:
           literals.append(literal)

     return pure_symbol_recursion

""" DELETE CLAUSES CONTAINING PURE SYMBOL"""
def pure_symbol_delete(clauses,check_literal):
    delete_clauses=[]
    for clause in clauses:
        if(clause[0]!="not"):
            for literal in clause:
                if(check_literal==literal):
                    delete_clauses.append(clause)
        elif(clause[0]=="not"):
            if(check_literal==clause):
                delete_clauses.append(clause)

    temp_clauses=[]
    for clause in clauses:
        flag=1
        for delete_clause in delete_clauses:
            if(clause==delete_clause):
                flag=0
        if flag==1:
            temp_clauses.append(clause)

    del clauses[:]
    for clause in temp_clauses:
        clauses.append(clause)

""" UNIT CLAUSES """
def unit_clauses(clauses,literals,truth_values,unit_clause_recursion):
    delete_literals=[]
    for clause in clauses:
        if(len(clause)==1):
            check_literal=clause[0]
            truth_value=check_literal+"=true"
            truth_values.append(truth_value)
            delete_literals.append(check_literal)
            unit_clause_delete_positive(clauses,check_literal)
        elif(len(clause)==2 and clause[0]=="not"):
            check_literal_1=clause
            check_literal=clause[1]
            truth_value=check_literal+"=false"
            truth_values.append(truth_value)
            delete_literals.append(check_literal)
            unit_clause_delete_negative(clauses,check_literal_1,check_literal)

   
    if(len(delete_literals)==0):
         unit_clause_recursion=0
    else:
       temp_literals=[]
       for literal in literals:
           flag=1
           for delete_literal in delete_literals:
              if(literal==delete_literal):
                  flag=0
           if flag==1:
              temp_literals.append(literal)
       
       del literals[:]
       for literal in temp_literals:
          literals.append(literal)

    return unit_clause_recursion

""" DELETE UNIT CLAUSES WHEN IT IS POSITIVE"""
def unit_clause_delete_positive(clauses,check_literal):
    delete_clauses=[]
    append_clauses=[]
    i=0
    for clause in clauses:
        if(len(clause)==1):
            if check_literal==clause:
                delete_clauses.append(clause)
        elif(len(clause)==2 and clause[0]=="not"):
            if check_literal==clause[1]:
               del clauses[i][1]
               del clauses[i][0]
        else:
            j=0
            for literal in clause:
                if(len(literal)==1):
                    if check_literal==literal:
                        delete_clauses.append(clause)
                elif(len(literal)==2 and literal[0]=="not"):
                    if check_literal==literal[1]:
                       del clauses[i][j]
                       if len(clause)==2 and clause[0]=="or":
                          delete_clauses.append(clause)
                          append_clauses.append(clause[1])
                j=j+1
        i=i+1

    temp_clauses=[]
    for clause in clauses:
        flag=1
        for delete_clause in delete_clauses:
            if(clause==delete_clause):
                flag=0
        if flag==1:
            temp_clauses.append(clause)

    del clauses[:]
    for clause in temp_clauses:
        clauses.append(clause)
   
    for clause in append_clauses:
        clauses.append(clause)

""" DELETE UNIT CLAUSES WHEN IT IS NEGATIVE"""
def unit_clause_delete_negative(clauses,check_literal,check_literal_positive):
    delete_clauses=[]
    append_clauses=[]
    insert_empty_clause=0
    i=0
    for clause in clauses:
        if(len(clause)==1):
            if check_literal_positive==clause:
                delete_clauses.append(clause)
                insert_empty_clause=1
        elif(len(clause)==2):
            if check_literal==clause:
               delete_clauses.append(clause)
        else:
            j=0
            for literal in clause:
                if(len(literal)==2):
                  if check_literal==literal:
                        delete_clauses.append(clause)
                elif(len(literal)==1):
                    if check_literal_positive==literal:
                       del clauses[i][j]
                       if len(clause)==2 and clause[0]=="or":
                          delete_clauses.append(clause)
                          append_clauses.append(clause[1])
                j=j+1
        i=i+1
    temp_clauses=[]
    for clause in clauses:
        flag=1
        for delete_clause in delete_clauses:
            if(clause==delete_clause):
                flag=0
        if flag==1:
            temp_clauses.append(clause)

    del clauses[:]    
    for clause in temp_clauses:
        clauses.append(clause)
    for clause in append_clauses:
        clauses.append(clause)
    if insert_empty_clause==1:
        clauses.append([])


""" WRITE TO OUTPUT FILE """
def writeOutput(final_list):
    filename='CNF_satisfiability.txt'
    outputFile = open(filename,'a')

    for sentence in final_list:
        sentence=str(sentence)
        sentence=sentence.replace("\'","\"")
        outputFile.write(sentence)
        outputFile.write("\n")
    
    outputFile.close()

""" CLEAR THE OUTPUT FILE """
def clear():
    filename='CNF_satisfiability.txt'
    outputFile = open(filename,'w')
    outputFile.truncate()
    outputFile.close()

""" READ THE INPUT FILE """
clear()
inputFile = open(sys.argv[2])
conf=0
line_number=0
final_list=[]
for line in inputFile:
    if conf==0:
        spl = line.strip().split(' ')
        line_number=int(spl[0])
        conf=1
    else:
        sentence=DPLL(line)
        final_list.append(sentence)
                    
inputFile.close()
writeOutput(final_list)


















