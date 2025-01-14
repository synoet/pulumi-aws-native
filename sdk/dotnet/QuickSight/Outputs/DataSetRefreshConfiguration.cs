// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    /// <summary>
    /// &lt;p&gt; Refresh Configuration.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class DataSetRefreshConfiguration
    {
        public readonly Outputs.DataSetIncrementalRefresh? IncrementalRefresh;

        [OutputConstructor]
        private DataSetRefreshConfiguration(Outputs.DataSetIncrementalRefresh? incrementalRefresh)
        {
            IncrementalRefresh = incrementalRefresh;
        }
    }
}
