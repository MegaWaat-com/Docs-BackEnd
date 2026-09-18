import os

STRUCTURE = {
    "01-user-management": [
        "auth-registration", "account-blocking", "flagging-system",
        "identity-verification", "access-roles-permissions",
        "profile-management", "address-book", "agency-branches"
    ],
    "02-product-catalog": [
        "specifications", "official-documents", "units-of-measure",
        "part-numbers", "creation-lifecycle", "external-integration", "media-assets"
    ],
    "03-project-catalog": [
        "template-fields", "specifications"
    ],
    "04-ads": [
        "lifecycle", "pricing-schemes", "insurance-warranty",
        "verification-documents", "review-approval", "lock-and-reserve",
        "expert-inspection", "delivery-terms", "project-listings",
        "sell-buy-requests", "rent-requests", "partnership"
    ],
    "05-negotiation-room": [
        "negotiation-rooms", "data-masking", "admin-oversight", "archive-history"
    ],
    "06-contract-common": [
        "final-approval", "audit-change-log", "invoicing", "amendments"
    ],
    "07-sales-contract": [
        "snapshot-state", "payments-escrow", "shipping-logistics",
        "inspection-handover", "return-process", "delay-penalty-damages"
    ],
    "08-rental-contract": [
        "timeline-schedule", "pricing-deposit", "handover-return-terms",
        "maintenance-repair", "insurance", "payments-escrow"
    ],
    "09-partnership-contract": [
        "capital-contributions", "profit-loss-sharing", "governance-signoff", "exit-strategy"
    ],
    "10-project-contract": [
        "scope-commitments", "project-timeline", "milestone-payments",
        "contract-amendments", "payments-escrow"
    ],
    "11-academy": [
        "courses-curriculum", "field-experiences", "qna-discussions",
        "certifications", "instructor-payouts"
    ],
    "12-experts-and-services": [
        "screening-assessment", "expert-profile", "specializations",
        "expertise-levels", "task-dispatch", "compensation-fee", "service-calendar"
    ],
    "13-finance-and-wallet": [
        "double-entry-accounting", "deposit-withdrawal", "payment-gateways",
        "wallet-freeze-escrow", "platform-fees"
    ],
    "14-platform-commons": [
        "file-city-storage", "notifications-engine", "numbering-schemes",
        "audit-logs", "live-chat-engine", "disaster-backup",
        "security-compliance", "infrastructure-server", "search-filtering",
        "taxonomy-categories", "print-document-generator", "idempotency-guard",
        "dispute-arbitration"
    ]
}

def create_structure():
    for root_dir, subdirs in STRUCTURE.items():
        for sub in subdirs:
            path = os.path.join(root_dir, sub)
            os.makedirs(path, exist_ok=True)
    print("✓ تمام فولدرها و زیربخش‌های مگاوات با موفقیت ساخته شدند.")

if __name__ == "__main__":
    create_structure()
