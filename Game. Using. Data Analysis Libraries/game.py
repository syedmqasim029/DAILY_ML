import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt





np.random.seed(42)

print("=" * 55)
print("              DATA DETECTIVE")
print("=" * 55)




print("""
CASE #001: THE STOLEN LAPTOP

A laptop was stolen from the university AI lab.

There are 6 suspects:
Ali, Ahmed, Bilal, Hamza, Daniyal, Saad

Your job is to analyze the crime data and find the culprit.

You have 6 clues to investigate.
Use DATA ANALYSIS to solve the case.
""")




suspects = [
    "Ali", "Ahmed", "Bilal", "Hamza",
    "Daniyal", "Saad"
]





records = []



for i in range(40):

    suspect = np.random.choice(suspects)

    # Normal random data
    time_in_lab = np.random.randint(10, 100)
    access_card = np.random.choice(["Yes", "No"])
    cctv_seen = np.random.choice(["Yes", "No"])
    suspicious = np.random.choice(["Yes", "No"])
    distance = np.random.randint(20, 100)

    records.append([
        suspect,
        time_in_lab,
        access_card,
        cctv_seen,
        suspicious,
        distance
    ])






df = pd.DataFrame(
    records,
    columns=[
        "Suspect",
        "Time_In_Lab",
        "Access_Card",
        "CCTV_Seen",
        "Suspicious_Activity",
        "Distance_From_Lab"
    ]
)






hamza_rows = df[df["Suspect"] == "Hamza"].index[:5]

df.loc[hamza_rows, "Time_In_Lab"] = [110, 105, 115, 108, 112]
df.loc[hamza_rows, "Access_Card"] = "Yes"
df.loc[hamza_rows, "CCTV_Seen"] = "Yes"
df.loc[hamza_rows, "Suspicious_Activity"] = "Yes"
df.loc[hamza_rows, "Distance_From_Lab"] = [5, 8, 10, 6, 7]





df["Suspicion_Score"] = (
    df["Access_Card"].eq("Yes").astype(int) * 25
    + df["CCTV_Seen"].eq("Yes").astype(int) * 25
    + df["Suspicious_Activity"].eq("Yes").astype(int) * 30
    + (df["Distance_From_Lab"] < 20).astype(int) * 20
)




print("\nCRIME DATA:")
print(df)



while True:

    print("""
=======================================================
                    DETECTIVE MENU
=======================================================

1. Check Access Card Clue
2. Check Suspicious Activity
3. Count Suspect Records
4. Find Average Suspicion Score
5. Find Most Suspicious Records
6. Show Correlation Heatmap
7. Final Investigation
8. Show Full Dataset
9. Exit

=======================================================
""")




    choice = input("Choose a clue (1-9): ")

   
    if choice == "1":

        print("\nCLUE 1: PEOPLE WITH ACCESS CARDS")
        print("-" * 40)

        result = df[df["Access_Card"] == "Yes"]

        print(result[[
            "Suspect",
            "Access_Card",
            "Time_In_Lab"
        ]])

        print("\nThink:")
        print("Who had access to the lab?")



    elif choice == "2":

        print("\nCLUE 2: SUSPICIOUS ACTIVITY")
        print("-" * 40)

        result = df[
            df["Suspicious_Activity"] == "Yes"
        ]

        print(result[[
            "Suspect",
            "Suspicious_Activity",
            "CCTV_Seen"
        ]])

        print("\nThink:")
        print("Which suspect appears suspicious multiple times?")






    elif choice == "3":

        print("\nCLUE 3: SUSPECT FREQUENCY")
        print("-" * 40)

        result = (
            df.groupby("Suspect")
            .size()
            .sort_values(ascending=False)
        )

        print(result)

        print("\nThink:")
        print("Which suspect appears most often?")




    elif choice == "4":

        print("\nCLUE 4: AVERAGE SUSPICION SCORE")
        print("-" * 40)

        result = (
            df.groupby("Suspect")["Suspicion_Score"]
            .mean()
            .sort_values(ascending=False)
        )

        print(result.round(2))

        print("\nThink:")
        print("Who has the highest average suspicion score?")



    elif choice == "5":

        print("\nCLUE 5: MOST SUSPICIOUS RECORDS")
        print("-" * 40)

        result = df[
            df["Suspicion_Score"] >= 70
        ]

        print(result[[
            "Suspect",
            "Time_In_Lab",
            "Access_Card",
            "CCTV_Seen",
            "Suspicious_Activity",
            "Distance_From_Lab",
            "Suspicion_Score"
        ]].sort_values(
            "Suspicion_Score",
            ascending=False
        ))



        print("\nThink:")
        print("Which suspect appears repeatedly in these records?")



    elif choice == "6":

        print("\nCLUE 6: CORRELATION HEATMAP")
        print("-" * 40)

        corr = df.select_dtypes(
            include="number"
        ).corr()

        print(corr.round(2))

        plt.figure(figsize=(8, 5))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Crime Data Correlation")
        plt.tight_layout()
        plt.show()

        print("\nLook for relationships with Suspicion_Score.")




    elif choice == "7":

        print("\n")
        print("=" * 55)
        print("              FINAL INVESTIGATION")
        print("=" * 55)

        final_evidence = df[
            (df["Access_Card"] == "Yes") &
            (df["CCTV_Seen"] == "Yes") &
            (df["Suspicious_Activity"] == "Yes") &
            (df["Distance_From_Lab"] < 20)
        ]

        print("\nFINAL EVIDENCE:")
        print(final_evidence[[
            "Suspect",
            "Time_In_Lab",
            "Access_Card",
            "CCTV_Seen",
            "Suspicious_Activity",
            "Distance_From_Lab",
            "Suspicion_Score"
        ]])

        suspect_counts = (
            final_evidence["Suspect"]
            .value_counts()
        )

        print("\nEvidence Count:")
        print(suspect_counts)

        if len(suspect_counts) > 0:

            culprit = suspect_counts.idxmax()

            print("\n" + "=" * 55)
            print("                 CASE SOLVED")
            print("=" * 55)

            print(f"\nThe prime suspect is: {culprit}")

            if culprit == "Hamza":
                print("""
The evidence strongly points toward Hamza.

He repeatedly:
- Had access to the lab
- Was seen on CCTV
- Showed suspicious activity
- Was very close to the lab

You solved the case using DATA ANALYSIS.
""")
            else:
                print("\nInvestigate the evidence again.")

        else:
            print("\nNo strong evidence found.")




    elif choice == "8":

        print("\nFULL CRIME DATA:")
        print(df)


    elif choice == "9":

        print("\nCase closed.")
        print("Good work, Detective.")
        break



    else:

        print("\nInvalid choice.")
        print("Choose a number from 1 to 9.")