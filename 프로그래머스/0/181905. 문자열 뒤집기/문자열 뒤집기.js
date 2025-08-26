function solution(my_string, s, e) {
    var answer = my_string.slice(0, s) + my_string.slice(s, e+1).split("").reverse().join("") + my_string.slice(e+1);
    
    return answer;
}