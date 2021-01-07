// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.LicenseManager.Outputs
{

    [OutputType]
    public sealed class LicenseProvisionalConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes
        /// </summary>
        public readonly int MaxTimeToLiveInMinutes;

        [OutputConstructor]
        private LicenseProvisionalConfiguration(int MaxTimeToLiveInMinutes)
        {
            this.MaxTimeToLiveInMinutes = MaxTimeToLiveInMinutes;
        }
    }
}