// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.LicenseManager.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-filterlist.html
    /// </summary>
    public sealed class LicenseFilterListArgs : Pulumi.ResourceArgs
    {
        [Input("FilterList")]
        private InputList<Inputs.LicenseFilterArgs>? _FilterList;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-filterlist.html#cfn-licensemanager-license-filterlist-filterlist
        /// </summary>
        public InputList<Inputs.LicenseFilterArgs> FilterList
        {
            get => _FilterList ?? (_FilterList = new InputList<Inputs.LicenseFilterArgs>());
            set => _FilterList = value;
        }

        public LicenseFilterListArgs()
        {
        }
    }
}