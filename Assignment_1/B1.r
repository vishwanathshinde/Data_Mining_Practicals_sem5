rev_number <- function(n) {
    rev1 = 0
    sum = 0
    r = 0
    while(n > 0) 
    {
        r = n %% 10
        sum = sum + r
        rev1 = rev1 * 10 + r
        n = n %/% 10
    }
    cat(paste("Reverse No is: ", rev1))
    cat(paste("Sum of digit is: ", sum))
}
rev_number(123)