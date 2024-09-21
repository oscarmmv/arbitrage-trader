import json

# Load UFC MMA data from JSON
with open('data/ufc_mma.json') as f:
    matches = json.load(f)

def convert_odds(odds):
    """Convert American odds to decimal odds."""
    if odds.startswith('+'):
        return float(odds[1:]) / 100 + 1
    elif odds.startswith('-'):
        return 100 / float(odds[1:]) + 1
    else:
        return None



def calculate_arbitrage(matches):
    idasdas = 0
    for match in matches:
        fighters = list(match.keys())
        fighter1 = fighters[0]
        fighter2 = fighters[1]

        odds1 = [convert_odds(odds) for odds in match[fighter1].values() if odds is not None]
        odds2 = [convert_odds(odds) for odds in match[fighter2].values() if odds is not None]

        if odds1 and odds2:
            best_odds1 = max(odds1)
            best_odds2 = max(odds2)

            # Calculate the arbitrage opportunity
            arbitrage_ratio = 1 / best_odds1 + 1 / best_odds2
            
            print(f"Match: {fighter1} vs {fighter2}")
            print(f"Best Odds for {fighter1}: {best_odds1:.2f}")
            print(f"Best Odds for {fighter2}: {best_odds2:.2f}")
            print(f"Arbitrage Ratio: {arbitrage_ratio:.4f}")
            
            if arbitrage_ratio < 1:
                profit = (1 - arbitrage_ratio) * 100
                print(f"Arbitrage Opportunity Exists! Potential Profit: ${profit:.2f}\n")
            else:
                print("No Arbitrage Opportunity.\n")
                idasdas += 1
                print(idasdas)
        else:
            print(f"Not enough odds for {fighter1} vs {fighter2}\n")
           

# Call the function to calculate arbitrage
calculate_arbitrage(matches)
