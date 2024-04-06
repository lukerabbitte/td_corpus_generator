import pandas as pd
import json

# Assuming the results are stored in a variable called results
results = {
    "enda-dail-comments": {
        "log10 text length": {
            "value": 5.134186673429167
        },
        "type-token ratio (disjoint windows)": {
            "value": 0.3902205882352941,
            "stdev": 0.007018384404831303
        },
        "evenness (disjoint windows)": {
            "value": 0.8709035214648928,
            "stdev": 0.001789661616926277
        },
        "average token length (disjoint windows)": {
            "value": 4.456808823529411,
            "stdev": 0.028654272078980917
        },
        "Gini-based dispersion (disjoint windows)": {
            "value": 0.39996426925455264,
            "stdev": 0.007813382893658365
        },
        "evenness-based dispersion (disjoint windows)": {
            "value": 0.6524760838834708,
            "stdev": 0.00844061793081749
        },
        "lexical density": {
            "value": 0.4267747406444792
        },
        "rarity": {
            "value": 0.15111478117258464
        },
        "average sentence length (words)": {
            "value": 21.814362907442913,
            "stdev": 13.975167858865863
        },
        "punctuation per sentence": {
            "value": 1.9267910057521354,
            "stdev": 1.5991876109654968
        },
        "average sentence length (tokens)": {
            "value": 23.74115391319505,
            "stdev": 15.032870849921778
        },
        "average dependency distance": {
            "value": 3.1464038409120465,
            "stdev": 0.810819249444947
        },
        "closeness centrality": {
            "value": 0.4439266511129575,
            "stdev": 0.1778166288799191
        },
        "dependents per word": {
            "value": 0.9383585159397774,
            "stdev": 0.04595610334684241
        }
    },
    "formal-articles": {
        "log10 text length": {
            "value": 5.143217840132094
        },
        "type-token ratio (disjoint windows)": {
            "value": 0.43145323741007197,
            "stdev": 0.00510813163249178
        },
        "evenness (disjoint windows)": {
            "value": 0.8922193406946625,
            "stdev": 0.001366787259809011
        },
        "average token length (disjoint windows)": {
            "value": 4.444726618705036,
            "stdev": 0.037220025646165715
        },
        "Gini-based dispersion (disjoint windows)": {
            "value": 0.38609200170599894,
            "stdev": 0.007838495831860273
        },
        "evenness-based dispersion (disjoint windows)": {
            "value": 0.6335677018642699,
            "stdev": 0.008547751674995952
        },
        "lexical density": {
            "value": 0.39654837665839715
        },
        "rarity": {
            "value": 0.2019004098212019
        },
        "average sentence length (words)": {
            "value": 20.911193029490615,
            "stdev": 11.758098466808244
        },
        "punctuation per sentence": {
            "value": 2.390583109919571,
            "stdev": 1.7247569260506512
        },
        "average sentence length (tokens)": {
            "value": 23.301776139410187,
            "stdev": 12.870716943746384
        },
        "average dependency distance": {
            "value": 3.24754679200939,
            "stdev": 0.8981966233190417
        },
        "closeness centrality": {
            "value": 0.4511534978740927,
            "stdev": 0.1813397644085054
        },
        "dependents per word": {
            "value": 0.9264903113891166,
            "stdev": 0.11621447241616477
        }
    },
    "social-comments": {
        "log10 text length": {
            "value": 5.154098206189118
        },
        "type-token ratio (disjoint windows)": {
            "value": 0.48188028169014085,
            "stdev": 0.0046697813752592035
        },
        "evenness (disjoint windows)": {
            "value": 0.9022497543568486,
            "stdev": 0.0011798337219203565
        },
        "average token length (disjoint windows)": {
            "value": 4.095323943661972,
            "stdev": 0.02160315001932893
        },
        "Gini-based dispersion (disjoint windows)": {
            "value": 0.41038953820148855,
            "stdev": 0.004944709131061028
        },
        "evenness-based dispersion (disjoint windows)": {
            "value": 0.6568302127250175,
            "stdev": 0.005357429679237693
        },
        "lexical density": {
            "value": 0.46321348172771454
        },
        "rarity": {
            "value": 0.2428729315226113
        },
        "average sentence length (words)": {
            "value": 14.61485260770975,
            "stdev": 11.989131480168078
        },
        "punctuation per sentence": {
            "value": 1.5521541950113378,
            "stdev": 1.2907606053316332
        },
        "average sentence length (tokens)": {
            "value": 16.167006802721087,
            "stdev": 12.729351851879674
        },
        "average dependency distance": {
            "value": 2.8181567278366475,
            "stdev": 0.9857691956074909
        },
        "closeness centrality": {
            "value": 0.5741277025678055,
            "stdev": 0.22017805718091596
        },
        "dependents per word": {
            "value": 0.8905968372085604,
            "stdev": 0.11839845934385375
        }
    },
}

data = []

for file, measures in results.items():
    for measure, values in measures.items():
        row = {"File": file, "Measure": measure}
        row.update(values)
        data.append(row)

df = pd.DataFrame(data)

# Save to TSV
df.to_csv("results.tsv", sep="\t", index=False)