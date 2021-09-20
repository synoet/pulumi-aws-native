// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner.Outputs
{

    /// <summary>
    /// Image Repository
    /// </summary>
    [OutputType]
    public sealed class ServiceImageRepository
    {
        public readonly Outputs.ServiceImageConfiguration? ImageConfiguration;
        /// <summary>
        /// Image Identifier
        /// </summary>
        public readonly string ImageIdentifier;
        /// <summary>
        /// Image Repository Type
        /// </summary>
        public readonly Pulumi.AwsNative.AppRunner.ServiceImageRepositoryImageRepositoryType ImageRepositoryType;

        [OutputConstructor]
        private ServiceImageRepository(
            Outputs.ServiceImageConfiguration? imageConfiguration,

            string imageIdentifier,

            Pulumi.AwsNative.AppRunner.ServiceImageRepositoryImageRepositoryType imageRepositoryType)
        {
            ImageConfiguration = imageConfiguration;
            ImageIdentifier = imageIdentifier;
            ImageRepositoryType = imageRepositoryType;
        }
    }
}
