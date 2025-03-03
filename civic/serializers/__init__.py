# Sector serializers
from civic.serializers.sector import DepartmentSerializer
from civic.serializers.sector import DepartmentSelectSerializer
from civic.serializers.sector import DepartmentDetailSerializer
from civic.serializers.sector import DepartmentUpdateSerializer
from civic.serializers.sector import DepartmentListSerializer

# Category serializers
from civic.serializers.category import CategorySerializer
from civic.serializers.category import CategorySelectSerializer
from civic.serializers.category import CategoryUpdateSerializer

# Complaint serializers
from civic.serializers.complaint import ComplaintRegisterSerializer
from civic.serializers.complaint import ComplaintListSerializer
from civic.serializers.complaint import ComplaintDetailSerializer
from civic.serializers.complaint import ComplaintStatusUpdateSerializer

# Demand letter serializers
from civic.serializers.demand_letter import DemandLetterRegisterSerializer
from civic.serializers.demand_letter import DemandLetterListSerializer
from civic.serializers.demand_letter import DemandLetterDetailSerializer
from civic.serializers.demand_letter import DemandLetterStatusUpdateSerializer

# Suggestion serializers
from civic.serializers.suggestion import SuggestionRegisterSerializer
from civic.serializers.suggestion import SuggestionListSerializer
from civic.serializers.suggestion import SuggestionDetailSerializer
from civic.serializers.suggestion import SuggestionStatusUpdateSerializer

# Geo location serializers
from civic.serializers.geolocation_complaint import (
    GeoLocationComplaintRegisterSerializer,
)
from civic.serializers.geolocation_complaint import GeoLocationComplaintListSerializer
from civic.serializers.geolocation_complaint import GeolocationComplaintDetailSerializer
from civic.serializers.geolocation_complaint import (
    GeolocationComplaintStatusUpdateSerializer,
)

# Scheme serializers
from civic.serializers.scheme import SchemeListSerializer
from civic.serializers.scheme import SchemeDetailSerializer
from civic.serializers.scheme import SchemeUpdateSerializer
from civic.serializers.scheme import SchemeRegisterSerializer
from civic.serializers.scheme import SchemeSelectSerializer
