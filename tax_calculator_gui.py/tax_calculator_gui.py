from breezypythongui import EasyFrame

class TaxCalculatorGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")

        # Input label and field
        self.addLabel(text="Enter Income:", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        # Button
        self.computeButton = self.addButton(
            text="Calculate Tax",
            row=1,
            column=0,
            columnspan=2,
            command=self.calculateTax
        )

        # Output labels and fields
        self.addLabel(text="Tax:", row=2, column=0)
        self.taxField = self.addFloatField(value=0.0, row=2, column=1)

        self.addLabel(text="Net Income:", row=3, column=0)
        self.netIncomeField = self.addFloatField(value=0.0, row=3, column=1)

    def calculateTax(self):
        try:
            income = self.incomeField.getNumber()
            taxRate = 0.20
            tax = income * taxRate
            netIncome = income - tax

            self.taxField.setNumber(tax)
            self.netIncomeField.setNumber(netIncome)

        except ValueError:
            self.messageBox(title="Error", message="Invalid input")

def main():
    TaxCalculatorGUI().mainloop()

if __name__ == "__main__":
    main()