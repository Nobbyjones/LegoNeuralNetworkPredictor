import csv

def parse_val(val):
    # Return None for NA / missing representation
    if val in ('NA', 'NaN', '', 'nan'):
        return None
    try:
        f = float(val)
        # Convert to int if float has no decimal part, otherwise keep as float
        return int(f) if f.is_integer() else f
    except ValueError:
        # Return original string if it cannot be converted to a number
        return val

def loadDataset():
    with open('lego_population.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)

        # Apply parse_val to item_number (key) and each attribute in row[1:]
        legoDataset = {
            parse_val(row[0]): [parse_val(val) for val in row[1:]]
            for row in reader if row
        }

    print("CSV module output sample:")
    first_key = list(legoDataset.keys())[0]
    print(f"Key ({type(first_key).__name__}): {first_key}")
    print(f"Attribute Values: {legoDataset[first_key]}")

    noOfPieces = legoDataset[first_key][2]
    yearOfRelease = legoDataset[first_key][5]
    noOfPiecesWeight = 0.1
    yearOfReleaseWeight = 0.02
    bias = 5
    learningSpeed = 0.00000001


    prediction = (noOfPieces * noOfPiecesWeight) + (yearOfRelease * yearOfReleaseWeight) + bias
    for j in range(500):
        if legoDataset[first_key][3] != None:
            for i in range(500):

                loss = 2*(prediction - legoDataset[first_key][3])

                piecesVar = loss * noOfPieces
                yearVar = loss * yearOfRelease
                biasVar = loss

                noOfPiecesWeight = noOfPiecesWeight - (learningSpeed * piecesVar)
                yearOfReleaseWeight = yearOfReleaseWeight - (learningSpeed * yearVar)
                bias = bias - (learningSpeed * biasVar)

                prediction = (noOfPieces * noOfPiecesWeight) + (yearOfRelease * yearOfReleaseWeight) + bias
        first_key = list(legoDataset.keys())[j]
        print(round(prediction, 2))



loadDataset()

