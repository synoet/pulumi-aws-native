// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceWebCrawlerSiteMapsConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("siteMaps", required: true)]
        private InputList<string>? _siteMaps;
        public InputList<string> SiteMaps
        {
            get => _siteMaps ?? (_siteMaps = new InputList<string>());
            set => _siteMaps = value;
        }

        public DataSourceWebCrawlerSiteMapsConfigurationArgs()
        {
        }
        public static new DataSourceWebCrawlerSiteMapsConfigurationArgs Empty => new DataSourceWebCrawlerSiteMapsConfigurationArgs();
    }
}
