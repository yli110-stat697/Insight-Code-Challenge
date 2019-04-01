import csv


def get_csv_file_ready(file_path, column_1, column_2):
    features = [] # this is the header of the csv file
    result = []  # this is the content of the csv file without the header

    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        features = csvreader.__next__()
        for row in csvreader:
            result.append([int(row[column_1]), int(row[column_2])])
    return result


products = get_csv_file_ready('./input/products.csv', 0, 3)
orders = get_csv_file_ready('./input/order_products.csv', 1, 3)


def sort_list(lst, n):
    lst.sort(key=lambda x:x[n])
    return lst


def match_join(orders, products):
    sort_list(orders, 0)
    sort_list(products, 0)

    j = 0
    for i in range(len(orders)):
        while orders[i][0] != products[j][0]:
            j += 1
            if j >= len(products):
                print("Product in the order doesn't belong to any department")
                break
        else:
            orders[i].append(products[j][1])
    return orders


data = match_join(orders,products)
data = sort_list(data, 2)


def output_row_ready(department_id, total, sum1):
    """
    Convert the desired output into one string with correct format, so that it can be write into the output csv.
    """
    sum0 = total - sum1
    percent = format(sum0/total, '.2f')
    output_row = [department_id, total, sum0, percent]
    return output_row

with open('./output/report.csv', 'w') as file:
    csvwriter = csv.writer(file, delimiter=',')
    csvwriter.writerow(['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage'])

    total = 1
    sum1 = data[0][1]

    for i in range(1, len(data)):
        if data[i][2] != data[i-1][2]:
            csvwriter.writerow(output_row_ready(data[i-1][2], total, sum1))

            total = 1
            sum1 = data[i][1]
        else:
            total += 1
            sum1 += data[i][1]
    csvwriter.writerow(output_row_ready(data[i][2], total, sum1))
