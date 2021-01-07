// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Greengrass.Outputs
{

    [OutputType]
    public sealed class FunctionDefinitionFunctionDefinitionVersion
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig
        /// </summary>
        public readonly Outputs.FunctionDefinitionDefaultConfig? DefaultConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-functions
        /// </summary>
        public readonly ImmutableArray<Outputs.FunctionDefinitionFunction> Functions;

        [OutputConstructor]
        private FunctionDefinitionFunctionDefinitionVersion(
            Outputs.FunctionDefinitionDefaultConfig? DefaultConfig,

            ImmutableArray<Outputs.FunctionDefinitionFunction> Functions)
        {
            this.DefaultConfig = DefaultConfig;
            this.Functions = Functions;
        }
    }
}