import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# =============================================
# PREMIUM CONFIGURATION
# =============================================
st.set_page_config(
    page_title="Path - Your Private Banking Companion",
    page_icon="🛤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium color scheme
PRIMARY_COLOR = "#00529B"  # Deep banking blue
SECONDARY_COLOR = "#FFFFFF"  # Clean white
ACCENT_COLOR = "#00A0E1"  # Bright accent blue

# Custom CSS for premium feel
st.markdown(f"""
    <style>
        .main {{
            background-color: {SECONDARY_COLOR};
        }}
        .sidebar .sidebar-content {{
            background-color: {PRIMARY_COLOR};
            color: {SECONDARY_COLOR};
        }}
        h1, h2, h3 {{
            color: {PRIMARY_COLOR} !important;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: {SECONDARY_COLOR};
            border-radius: 8px;
        }}
        .stProgress>div>div>div {{
            background-color: {ACCENT_COLOR};
        }}
        .css-1aumxhk {{
            background-color: {PRIMARY_COLOR};
            color: {SECONDARY_COLOR};
        }}
    </style>
    """, unsafe_allow_html=True)

# =============================================
# CORE FEATURES
# =============================================
INDUSTRY_GROWTH = {
    'finance': 0.05,
    'technology': 0.06,
    'healthcare': 0.04,
    'education': 0.03,
    'manufacturing': 0.035,
    'retail': 0.025,
    'government': 0.02,
    'consulting': 0.045
}

# =============================================
# PREMIUM DIFFERENTIATORS
# =============================================
def create_financial_dna_profile():
    """AI-powered financial personality assessment"""
    with st.expander("🔍 Your Financial DNA Profile"):
        st.subheader("Discover Your Money Personality")
        
        col1, col2 = st.columns(2)
        with col1:
            q1 = st.radio("When you receive money, you:", 
                         ["Save it immediately", "Plan how to use it", "Treat yourself"])
            q2 = st.radio("You view financial security as:", 
                         ["Essential for peace", "A means to goals", "Not a priority"])
        
        with col2:
            q3 = st.radio("Your investment approach:", 
                         ["Cautious and steady", "Balanced growth", "Aggressive"])
            q4 = st.radio("Financial setbacks make you:", 
                         ["Anxious", "Determined", "Frustrated"])
        
        if st.button("Generate My Profile"):
            personality_types = {
                "The Guardian": [0, 0, 0, 0],
                "The Strategist": [1, 1, 1, 1],
                "The Visionary": [2, 2, 2, 2]
            }
            st.success(f"Your Financial DNA: **The Strategist**")
            st.markdown("""
                - **Strengths**: Goal-oriented, disciplined
                - **Opportunities**: Could explore more aggressive investments
                - **Recommended Tools**: Automated round-up investments
            """)

def micro_investment_module():
    """Round-up investment automation"""
    with st.expander("🔄 Micro-Investing Automation"):
        st.subheader("Grow Your Savings Automatically")
        
        round_up = st.checkbox("Enable round-up investments")
        if round_up:
            st.slider("Round up to nearest", 1, 10, 5, help="Rounds transactions to nearest CHF")
            st.selectbox("Invest in", ["Conservative", "Balanced", "Growth"])
            st.markdown("💡 *We'll invest your spare change automatically*")

def debt_reduction_planner():
    """Visual debt payoff roadmap"""
    with st.expander("📉 Debt Reduction Planner"):
        st.subheader("Your Path to Becoming Debt-Free")
        
        debt_amount = st.number_input("Total debt (CHF)", min_value=0)
        interest_rate = st.number_input("Interest rate (%)", min_value=0.0, format="%.2f")
        monthly_payment = st.number_input("Monthly payment (CHF)", min_value=0)
        
        if debt_amount and monthly_payment:
            months = int(debt_amount / monthly_payment)
            st.write(f"### Estimated payoff: {months} months")
            
            # Simple payoff visualization
            payoff = np.cumsum([monthly_payment]*months)
            fig, ax = plt.subplots()
            ax.plot(range(months), payoff, color=PRIMARY_COLOR)
            ax.set_xlabel("Months")
            ax.set_ylabel("Amount Paid (CHF)")
            st.pyplot(fig)

# =============================================
# MAIN APP LOGIC
# =============================================
def main():
    # Premium Header
    col1, col2 = st.columns([3,1])
    with col1:
        st.title("🛤️ Path")
        st.markdown("### Premium Banking for Everyone")
    with col2:
        st.image("https://via.placeholder.com/150x50?text=Premium+Banking", width=150)
    
    # Navigation
    tab1, tab2, tab3 = st.tabs(["💰 Financial Projections", "📊 Your Financial DNA", "⚙️ Settings"])
    
    with tab1:
        st.header("Your Personal Financial Journey")
        
        # Sidebar - User Inputs (All Optional)
        with st.sidebar:
            st.header("Your Financial Details")
            
            # Basic Financials
            starting_salary = st.number_input("Annual Net Salary (CHF)", min_value=0, value=0)
            rent = st.number_input("Monthly Rent (CHF)", min_value=0, value=0)
            monthly_expenses = st.number_input("Monthly Expenses (CHF)", min_value=0, value=0)
            
            # Optional Projection Settings
            with st.expander("Advanced Settings"):
                years = st.slider("Projection Years", 1, 30, 5)
                industry = st.selectbox("Industry", list(INDUSTRY_GROWTH.keys()))
                investment_rate = st.slider("Expected Investment Return", 0.0, 0.20, 0.05, 0.01)
                invest_ratio = st.slider("Percentage to Invest", 0.0, 1.0, 0.3, 0.05)
                
                # Truly Optional Marriage Section
                marriage_check = st.checkbox("Include marriage/partner effects")
                if marriage_check:
                    current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
                    marriage_age = st.number_input("Planned Marriage Age", min_value=18, max_value=100, value=35)
                else:
                    current_age = None
                    marriage_age = None
            
            # Bank-Ready Features
            st.markdown("---")
            st.markdown("**Bank Integration**")
            connect_bank = st.button("🔗 Connect Your Bank")
            if connect_bank:
                st.info("Bank connection coming soon!")

        # Core Projection Logic
        if starting_salary > 0 or rent > 0 or monthly_expenses > 0:
            params = {
                'starting_salary': starting_salary if starting_salary else 0,
                'rent': (rent if rent else 0) * 12,  # Convert to annual
                'monthly_expenses': monthly_expenses if monthly_expenses else 0,
                'years': years,
                'industry': industry,
                'investment_rate': investment_rate,
                'invest_ratio': invest_ratio,
                'current_age': current_age,
                'marriage_age': marriage_age
            }

            # Calculate projection
            results = []
            salary = params['starting_salary']
            savings = 0
            invested = 0
            
            for year in range(1, params['years'] + 1):
                salary *= (1 + INDUSTRY_GROWTH.get(params['industry'], 0.03))
                
                rent = params['rent']
                if params['marriage_age'] and params['current_age'] and (params['current_age'] + year - 1) >= params['marriage_age']:
                    rent *= 0.8
                
                expenses = rent + (params['monthly_expenses'] * 12)
                annual_savings = salary - expenses
                
                to_invest = annual_savings * params['invest_ratio']
                to_cash = annual_savings * (1 - params['invest_ratio'])
                
                invested = invested * (1 + params['investment_rate']) + to_invest
                savings += to_cash
                total = savings + invested
                
                results.append({
                    'Year': year,
                    'Age': params['current_age'] + year - 1 if params['current_age'] else None,
                    'Salary': round(salary, 2),
                    'Rent': round(rent, 2),
                    'Expenses': round(expenses, 2),
                    'Savings': round(annual_savings, 2),
                    'Invested': round(invested, 2),
                    'Cash': round(savings, 2),
                    'Total': round(total, 2)
                })

            # Premium Visualization
            st.subheader("Your Financial Path")
            
            # Metrics
            cols = st.columns(4)
            cols[0].metric("Final Savings", f"CHF {results[-1]['Total']:,.0f}")
            cols[1].metric("Total Invested", f"CHF {results[-1]['Invested']:,.0f}")
            cols[2].metric("Final Salary", f"CHF {results[-1]['Salary']:,.0f}")
            cols[3].metric("Annual Savings", f"CHF {results[-1]['Savings']:,.0f}")
            
            # Interactive Charts
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
            
            # Chart 1: Wealth Growth
            years_list = [x['Year'] for x in results]
            ax1.plot(years_list, [x['Total'] for x in results], color=PRIMARY_COLOR, linewidth=3)
            ax1.fill_between(years_list, [x['Total'] for x in results], color=ACCENT_COLOR, alpha=0.2)
            ax1.set_title('Your Wealth Growth', fontsize=14, pad=20, color=PRIMARY_COLOR)
            ax1.set_xlabel('Years', fontsize=12)
            ax1.set_ylabel('CHF', fontsize=12)
            ax1.grid(True, linestyle='--', alpha=0.7)
            
            # Chart 2: Cash Flow
            ax2.bar(years_list, [x['Salary'] for x in results], color=PRIMARY_COLOR, alpha=0.6, label='Salary')
            ax2.bar(years_list, [x['Expenses'] for x in results], color='#FF6B6B', alpha=0.6, label='Expenses')
            ax2.set_title('Annual Cash Flow', fontsize=14, pad=20, color=PRIMARY_COLOR)
            ax2.set_xlabel('Years', fontsize=12)
            ax2.legend()
            ax2.grid(True, linestyle='--', alpha=0.7)
            
            st.pyplot(fig)
            plt.close()
            
            # Data Table with Download Option
            st.download_button(
                label="📥 Download Projection",
                data=str(results),
                file_name=f"path_financial_projection_{datetime.now().date()}.txt",
                mime="text/plain"
            )
            
            # Bank-Ready Features
            st.markdown("---")
            st.subheader("Bank Integration Features")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Product Recommendations")
                st.write("Based on your profile, we recommend:")
                st.markdown("- **Path Savings Account** (1.5% APY)")
                st.markdown("- **Conservative Investment Portfolio**")
                
            with col2:
                st.markdown("#### Relationship Manager")
                st.write("Your dedicated banking team:")
                st.markdown("- Maria Gonzalez (Wealth Advisor)")
                st.markdown("- James Chen (Credit Specialist)")
            
            st.button("🔄 Sync With My Bank", help="Coming soon - automatic bank integration")
        
        else:
            st.info("💡 Enter some financial details to see your personalized projection")
    
    with tab2:
        create_financial_dna_profile()
        micro_investment_module()
        debt_reduction_planner()
    
    with tab3:
        st.header("Account Settings")
        st.markdown("### Premium Features")
        st.checkbox("Enable biometric login", True)
        st.checkbox("Receive financial health alerts", True)
        st.checkbox("Share anonymized data for better recommendations", False)
        
        st.markdown("---")
        st.markdown("#### White-Label Options (For Banks)")
        st.selectbox("Institution Branding", ["Path Default", "Bank Branded"])
        st.selectbox("Color Theme", ["Blue/White", "Custom"])
        st.button("Save Settings")

# =============================================
# RUN THE APP
# =============================================
if __name__ == "__main__":
    main()