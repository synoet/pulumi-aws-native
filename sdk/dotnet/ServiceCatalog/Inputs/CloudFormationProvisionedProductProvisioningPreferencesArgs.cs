// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ServiceCatalog.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html
    /// </summary>
    public sealed class CloudFormationProvisionedProductProvisioningPreferencesArgs : Pulumi.ResourceArgs
    {
        [Input("StackSetAccounts")]
        private InputList<string>? _StackSetAccounts;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts
        /// </summary>
        public InputList<string> StackSetAccounts
        {
            get => _StackSetAccounts ?? (_StackSetAccounts = new InputList<string>());
            set => _StackSetAccounts = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount
        /// </summary>
        [Input("StackSetFailureToleranceCount")]
        public Input<int>? StackSetFailureToleranceCount { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage
        /// </summary>
        [Input("StackSetFailureTolerancePercentage")]
        public Input<int>? StackSetFailureTolerancePercentage { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount
        /// </summary>
        [Input("StackSetMaxConcurrencyCount")]
        public Input<int>? StackSetMaxConcurrencyCount { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage
        /// </summary>
        [Input("StackSetMaxConcurrencyPercentage")]
        public Input<int>? StackSetMaxConcurrencyPercentage { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype
        /// </summary>
        [Input("StackSetOperationType")]
        public Input<string>? StackSetOperationType { get; set; }

        [Input("StackSetRegions")]
        private InputList<string>? _StackSetRegions;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions
        /// </summary>
        public InputList<string> StackSetRegions
        {
            get => _StackSetRegions ?? (_StackSetRegions = new InputList<string>());
            set => _StackSetRegions = value;
        }

        public CloudFormationProvisionedProductProvisioningPreferencesArgs()
        {
        }
    }
}