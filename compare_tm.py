import argparse
from parse_cpu_verbose import CPU_Verbose, sort_verbs, read_verbose 

def verbs_subtract(v1, v2):
    if len(v1) != len(v2):
        print(f"v1, v2 size mismatch. {len(v1)} vs {len(v2)}")
        exit()
    v3 = []
    compare_num = len(v1)
    # compare_num = min(len(v1), len(v2))
    for i in range(compare_num):
        v3.append(v1[i] - v2[i])
    return v3

# Input: CPU_Verbose[]
def del_elements_with_same_name(verbos:list):
    r = []
    last_name = []
    for v in (verbos):
        if v.new_name in last_name:
            continue
        last_name.append(v.new_name)
        r.append(v)
    return r

def Compare_verbs(fn1, fn2):
    print("============================")
    print(f"Compare: \n  {fn1}\n  VS\n  {fn2}")
    print(f"Time diff: p1 - p2, unit ms.")
    print("============================")
    verbs_1 = read_verbose(fn1)
    verbs_2 = read_verbose(fn2)

    v3 = verbs_subtract(verbs_1, verbs_2)
    v3 = sort_verbs(v3, True)
    v3.reverse()

    # Delete neighbor elements with the same name.
    v3 = del_elements_with_same_name(v3)

    # Show top N
    show_top = min(3, len(v3))
    # show_top = len(v3)
    for i in range(show_top):
        print(v3[i])


# Defining main function 
def main(): 
    parser = argparse.ArgumentParser(description ='Process some integers.')
    parser.add_argument('fn1', metavar ='1', 
                        type = str,
                        help ='verbose1 fn')
    
    parser.add_argument('fn2', metavar ='2', 
                        type = str,
                        help ='verbose2 fn')
    
    args = parser.parse_args()
    Compare_verbs(args.fn1, args.fn2)

if __name__=="__main__": 
    main() 

