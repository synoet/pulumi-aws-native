// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;Amazon Elasticsearch Service parameters.&lt;/p&gt;
    /// </summary>
    public sealed class DataSourceAmazonElasticsearchParametersArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Elasticsearch Service domain.&lt;/p&gt;
        /// </summary>
        [Input("domain", required: true)]
        public Input<string> Domain { get; set; } = null!;

        public DataSourceAmazonElasticsearchParametersArgs()
        {
        }
        public static new DataSourceAmazonElasticsearchParametersArgs Empty => new DataSourceAmazonElasticsearchParametersArgs();
    }
}
