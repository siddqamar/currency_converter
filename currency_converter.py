import streamlit as st

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    st.title("Currency Converter")

    # Get user input for amount
    amount = st.number_input("Enter amount:", min_value=0.0, step=0.01, format="%.2f")

    # Get exchange rates from the user
    euro_to_pkr_rate = st.number_input("Enter Euro to PKR exchange rate:")
    usd_to_pkr_rate = st.number_input("Enter USD to PKR exchange rate:")
    gbp_to_pkr_rate = st.number_input("Enter British Pound to PKR exchange rate:")

    # Calculate and display converted amounts
    euro_to_pkr = convert_currency(amount, euro_to_pkr_rate)
    usd_to_pkr = convert_currency(amount, usd_to_pkr_rate)
    gbp_to_pkr = convert_currency(amount, gbp_to_pkr_rate)

    st.success(f"{amount} Euro is equal to {euro_to_pkr:.2f} PKR")
    st.success(f"{amount} USD is equal to {usd_to_pkr:.2f} PKR")
    st.success(f"{amount} British Pound is equal to {gbp_to_pkr:.2f} PKR")

if __name__ == "__main__":
    main()
