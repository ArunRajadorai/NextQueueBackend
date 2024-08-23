import reducer from './store'
import { injectReducer } from '@/store'
import AdaptableCard from '@/components/shared/AdaptableCard'
import ShopTable from './components/ShopTable'
import ShopTableTools from './components/ShopTableTools'

injectReducer('salesProductList', reducer)

const ShopList = () => {
    return (
        <AdaptableCard className="h-full" bodyClass="h-full">
            <div className="lg:flex items-center justify-between mb-4">
                <h3 className="mb-4 lg:mb-0">Shops</h3>
                <ShopTableTools />
            </div>
            <ShopTable />
        </AdaptableCard>
    )
}

export default ShopList
