stud_name <- c("Ram", "Sham", "Karan", "Arjun")

# convert vector into factor
factor(stud_name)

stud_roll <- c(1, 2, 3, 4)

# convert vector into factor
factor(stud_roll)

# Combined factor
combined <- factor(c(stud_name, stud_roll))

print("Combined factor is: ")
print(combined)