emp.data <- data.frame(
    emp_id = c(1:4),
    emp_weight = c(100, 125, 144, 90),
    emp_height = c(170, 168, 190, 145),
    stringsAsFactors = FALSE
)
print(emp.data)

ans <- emp.data[emp.data$emp_weight > 120,]
print(ans)

data = emp.data
sorted_date = data[order(data$emp_weight),]
print(sorted_date)