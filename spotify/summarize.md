# Spotify Analysis: Subscription Type vs Usage Intensity

## Research Question

Does subscription type (Free, Premium, Family, Student) affect user engagement measured by:
- Skip rate
- Number of songs played per day
- Daily listening time

## Dataset

- 8,000 users
- 12 features
- 4 subscription types: Premium (26.4%), Free (25.2%), Student (24.5%), Family (23.8%)

## Key Findings

### 1. **Subscription type has minimal impact on usage patterns**

All groups show nearly identical behavior:

| Metric | Free | Premium | Family | Student |
|--------|------|---------|--------|---------|
| Skip rate (%) | 30.09 | 29.66 | 30.03 | 30.29 |
| Songs/day | 49.2 | 49.7 | 50.4 | 51.2 |
| Listening time (min) | 155.0 | 155.5 | 151.0 | 154.5 |

**Differences are negligible (< 2% variance across all metrics)**

### 2. **Free users are as engaged as Premium users**

- Free users listen just as long as Premium users (~155 minutes/day)
- Free users skip songs at the same rate as Premium (30.09% vs 29.66%)
- Free users represent 25% of the user base

### 3. **Student users show slightly higher engagement**

- Highest songs per day: 51.24 (vs ~50 for others)
- Possibly due to better price-to-value ratio

## Business Implications

1. **High conversion potential**: Free users are highly engaged but not paying
2. **Pricing question**: Why don't engaged Free users convert to Premium?
3. **Ads aren't blocking engagement**: Free users tolerate ads without changing behavior
4. **Student tier works well**: Price sensitivity + high engagement = successful segment

## Recommendation

Investigate conversion barriers for Free users - engagement is high, but monetization is low.