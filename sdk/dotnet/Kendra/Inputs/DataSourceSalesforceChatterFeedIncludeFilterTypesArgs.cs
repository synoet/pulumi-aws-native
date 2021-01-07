// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Kendra.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedincludefiltertypes.html
    /// </summary>
    public sealed class DataSourceSalesforceChatterFeedIncludeFilterTypesArgs : Pulumi.ResourceArgs
    {
        [Input("SalesforceChatterFeedIncludeFilterTypes")]
        private InputList<string>? _SalesforceChatterFeedIncludeFilterTypes;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedincludefiltertypes.html#cfn-kendra-datasource-salesforcechatterfeedincludefiltertypes-salesforcechatterfeedincludefiltertypes
        /// </summary>
        public InputList<string> SalesforceChatterFeedIncludeFilterTypes
        {
            get => _SalesforceChatterFeedIncludeFilterTypes ?? (_SalesforceChatterFeedIncludeFilterTypes = new InputList<string>());
            set => _SalesforceChatterFeedIncludeFilterTypes = value;
        }

        public DataSourceSalesforceChatterFeedIncludeFilterTypesArgs()
        {
        }
    }
}