def regra_operacional(row):
    if row['Contract'] == 'Month-to-month' and row['MonthlyCharges'] > 65.0:
        return 1
    return 0