from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    max_subscribers = -1
    max_sales = -1

    # 모든 할인율 조합에 대해 반복
    for discounts in product(discount_rates, repeat=len(emoticons)):
        total_subscribers = 0
        total_sales = 0
        
        # 각 사용자에 대해 반복
        for user in users:
            user_discount_rate, user_price_limit = user
            
            purchase_cost = 0
            
            # 각 이모티콘에 대해 반복
            for i in range(len(emoticons)):
                discount_rate = discounts[i]
                emoticon_price = emoticons[i]
                
                if discount_rate >= user_discount_rate:
                    discounted_price = emoticon_price * (100 - discount_rate) // 100
                    purchase_cost += discounted_price
            
            if purchase_cost >= user_price_limit:
                total_subscribers += 1 
            else:
                total_sales += purchase_cost
        
        if (total_subscribers > max_subscribers or (total_subscribers == max_subscribers and total_sales > max_sales)):
            max_subscribers = total_subscribers 
            max_sales=total_sales
    
    return [max_subscribers,max_sales]
