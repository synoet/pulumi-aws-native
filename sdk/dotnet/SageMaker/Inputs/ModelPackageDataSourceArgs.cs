// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Describes the input source of a transform job and the way the transform job consumes it.
    /// </summary>
    public sealed class ModelPackageDataSourceArgs : Pulumi.ResourceArgs
    {
        [Input("s3DataSource", required: true)]
        public Input<Inputs.ModelPackageS3DataSourceArgs> S3DataSource { get; set; } = null!;

        public ModelPackageDataSourceArgs()
        {
        }
    }
}
