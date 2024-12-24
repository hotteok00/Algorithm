def solution(myStr):
    separators = ["a", "b", "c"]
    
    for s in separators:
        myStr = myStr.replace(s, " ").strip()
    
    return [str_ for str_ in myStr.split(" ") if str_ != ""] if len(myStr) > 0 else ["EMPTY"]