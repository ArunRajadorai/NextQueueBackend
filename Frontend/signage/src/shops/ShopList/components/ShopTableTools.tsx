import Button from '@/components/ui/Button'
import { HiDownload, HiPlusCircle } from 'react-icons/hi'
import ShopTableSearch from './ShopTableSearch'
import ShopFilter from './ShopFilter'
import { Link } from 'react-router-dom'

const ShopTableTools = () => {
    return (
        <div className="flex flex-col lg:flex-row lg:items-center">
            <ShopTableSearch />
            <ShopFilter />
            <Link
                download
                className="block lg:inline-block md:mx-2 md:mb-0 mb-4"
                to="/data/product-list.csv"
                target="_blank"
            >
                <Button block size="sm" icon={<HiDownload />}>
                    Export
                </Button>
            </Link>
            <Link
                className="block lg:inline-block md:mb-0 mb-8"
                to="/app/sales/product-new"
            >
                <Button block variant="solid" size="sm" icon={<HiPlusCircle />}>
                    Add Shop
                </Button>
            </Link>
        </div>
    )
}

export default ShopTableTools
