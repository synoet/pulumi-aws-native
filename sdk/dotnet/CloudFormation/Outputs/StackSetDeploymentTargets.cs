// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation.Outputs
{

    /// <summary>
    ///  The AWS OrganizationalUnitIds or Accounts for which to create stack instances in the specified Regions.
    /// </summary>
    [OutputType]
    public sealed class StackSetDeploymentTargets
    {
        /// <summary>
        /// The filter type you want to apply on organizational units and accounts.
        /// </summary>
        public readonly Pulumi.AwsNative.CloudFormation.StackSetDeploymentTargetsAccountFilterType? AccountFilterType;
        /// <summary>
        /// AWS accounts that you want to create stack instances in the specified Region(s) for.
        /// </summary>
        public readonly ImmutableArray<string> Accounts;
        /// <summary>
        /// Returns the value of the AccountsUrl property.
        /// </summary>
        public readonly string? AccountsUrl;
        /// <summary>
        /// The organization root ID or organizational unit (OU) IDs to which StackSets deploys.
        /// </summary>
        public readonly ImmutableArray<string> OrganizationalUnitIds;

        [OutputConstructor]
        private StackSetDeploymentTargets(
            Pulumi.AwsNative.CloudFormation.StackSetDeploymentTargetsAccountFilterType? accountFilterType,

            ImmutableArray<string> accounts,

            string? accountsUrl,

            ImmutableArray<string> organizationalUnitIds)
        {
            AccountFilterType = accountFilterType;
            Accounts = accounts;
            AccountsUrl = accountsUrl;
            OrganizationalUnitIds = organizationalUnitIds;
        }
    }
}
