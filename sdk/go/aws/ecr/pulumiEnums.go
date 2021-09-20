// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The encryption type to use.
type RepositoryEncryptionType string

const (
	RepositoryEncryptionTypeAes256 = RepositoryEncryptionType("AES256")
	RepositoryEncryptionTypeKms    = RepositoryEncryptionType("KMS")
)

func (RepositoryEncryptionType) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryEncryptionType)(nil)).Elem()
}

func (e RepositoryEncryptionType) ToRepositoryEncryptionTypeOutput() RepositoryEncryptionTypeOutput {
	return pulumi.ToOutput(e).(RepositoryEncryptionTypeOutput)
}

func (e RepositoryEncryptionType) ToRepositoryEncryptionTypeOutputWithContext(ctx context.Context) RepositoryEncryptionTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(RepositoryEncryptionTypeOutput)
}

func (e RepositoryEncryptionType) ToRepositoryEncryptionTypePtrOutput() RepositoryEncryptionTypePtrOutput {
	return e.ToRepositoryEncryptionTypePtrOutputWithContext(context.Background())
}

func (e RepositoryEncryptionType) ToRepositoryEncryptionTypePtrOutputWithContext(ctx context.Context) RepositoryEncryptionTypePtrOutput {
	return RepositoryEncryptionType(e).ToRepositoryEncryptionTypeOutputWithContext(ctx).ToRepositoryEncryptionTypePtrOutputWithContext(ctx)
}

func (e RepositoryEncryptionType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryEncryptionType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryEncryptionType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RepositoryEncryptionType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type RepositoryEncryptionTypeOutput struct{ *pulumi.OutputState }

func (RepositoryEncryptionTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryEncryptionType)(nil)).Elem()
}

func (o RepositoryEncryptionTypeOutput) ToRepositoryEncryptionTypeOutput() RepositoryEncryptionTypeOutput {
	return o
}

func (o RepositoryEncryptionTypeOutput) ToRepositoryEncryptionTypeOutputWithContext(ctx context.Context) RepositoryEncryptionTypeOutput {
	return o
}

func (o RepositoryEncryptionTypeOutput) ToRepositoryEncryptionTypePtrOutput() RepositoryEncryptionTypePtrOutput {
	return o.ToRepositoryEncryptionTypePtrOutputWithContext(context.Background())
}

func (o RepositoryEncryptionTypeOutput) ToRepositoryEncryptionTypePtrOutputWithContext(ctx context.Context) RepositoryEncryptionTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RepositoryEncryptionType) *RepositoryEncryptionType {
		return &v
	}).(RepositoryEncryptionTypePtrOutput)
}

func (o RepositoryEncryptionTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o RepositoryEncryptionTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryEncryptionType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o RepositoryEncryptionTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryEncryptionTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryEncryptionType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type RepositoryEncryptionTypePtrOutput struct{ *pulumi.OutputState }

func (RepositoryEncryptionTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryEncryptionType)(nil)).Elem()
}

func (o RepositoryEncryptionTypePtrOutput) ToRepositoryEncryptionTypePtrOutput() RepositoryEncryptionTypePtrOutput {
	return o
}

func (o RepositoryEncryptionTypePtrOutput) ToRepositoryEncryptionTypePtrOutputWithContext(ctx context.Context) RepositoryEncryptionTypePtrOutput {
	return o
}

func (o RepositoryEncryptionTypePtrOutput) Elem() RepositoryEncryptionTypeOutput {
	return o.ApplyT(func(v *RepositoryEncryptionType) RepositoryEncryptionType {
		if v != nil {
			return *v
		}
		var ret RepositoryEncryptionType
		return ret
	}).(RepositoryEncryptionTypeOutput)
}

func (o RepositoryEncryptionTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryEncryptionTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *RepositoryEncryptionType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// RepositoryEncryptionTypeInput is an input type that accepts RepositoryEncryptionTypeArgs and RepositoryEncryptionTypeOutput values.
// You can construct a concrete instance of `RepositoryEncryptionTypeInput` via:
//
//          RepositoryEncryptionTypeArgs{...}
type RepositoryEncryptionTypeInput interface {
	pulumi.Input

	ToRepositoryEncryptionTypeOutput() RepositoryEncryptionTypeOutput
	ToRepositoryEncryptionTypeOutputWithContext(context.Context) RepositoryEncryptionTypeOutput
}

var repositoryEncryptionTypePtrType = reflect.TypeOf((**RepositoryEncryptionType)(nil)).Elem()

type RepositoryEncryptionTypePtrInput interface {
	pulumi.Input

	ToRepositoryEncryptionTypePtrOutput() RepositoryEncryptionTypePtrOutput
	ToRepositoryEncryptionTypePtrOutputWithContext(context.Context) RepositoryEncryptionTypePtrOutput
}

type repositoryEncryptionTypePtr string

func RepositoryEncryptionTypePtr(v string) RepositoryEncryptionTypePtrInput {
	return (*repositoryEncryptionTypePtr)(&v)
}

func (*repositoryEncryptionTypePtr) ElementType() reflect.Type {
	return repositoryEncryptionTypePtrType
}

func (in *repositoryEncryptionTypePtr) ToRepositoryEncryptionTypePtrOutput() RepositoryEncryptionTypePtrOutput {
	return pulumi.ToOutput(in).(RepositoryEncryptionTypePtrOutput)
}

func (in *repositoryEncryptionTypePtr) ToRepositoryEncryptionTypePtrOutputWithContext(ctx context.Context) RepositoryEncryptionTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(RepositoryEncryptionTypePtrOutput)
}

// The image tag mutability setting for the repository.
type RepositoryImageTagMutability string

const (
	RepositoryImageTagMutabilityMutable   = RepositoryImageTagMutability("MUTABLE")
	RepositoryImageTagMutabilityImmutable = RepositoryImageTagMutability("IMMUTABLE")
)

func (RepositoryImageTagMutability) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryImageTagMutability)(nil)).Elem()
}

func (e RepositoryImageTagMutability) ToRepositoryImageTagMutabilityOutput() RepositoryImageTagMutabilityOutput {
	return pulumi.ToOutput(e).(RepositoryImageTagMutabilityOutput)
}

func (e RepositoryImageTagMutability) ToRepositoryImageTagMutabilityOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityOutput {
	return pulumi.ToOutputWithContext(ctx, e).(RepositoryImageTagMutabilityOutput)
}

func (e RepositoryImageTagMutability) ToRepositoryImageTagMutabilityPtrOutput() RepositoryImageTagMutabilityPtrOutput {
	return e.ToRepositoryImageTagMutabilityPtrOutputWithContext(context.Background())
}

func (e RepositoryImageTagMutability) ToRepositoryImageTagMutabilityPtrOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityPtrOutput {
	return RepositoryImageTagMutability(e).ToRepositoryImageTagMutabilityOutputWithContext(ctx).ToRepositoryImageTagMutabilityPtrOutputWithContext(ctx)
}

func (e RepositoryImageTagMutability) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryImageTagMutability) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e RepositoryImageTagMutability) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e RepositoryImageTagMutability) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type RepositoryImageTagMutabilityOutput struct{ *pulumi.OutputState }

func (RepositoryImageTagMutabilityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RepositoryImageTagMutability)(nil)).Elem()
}

func (o RepositoryImageTagMutabilityOutput) ToRepositoryImageTagMutabilityOutput() RepositoryImageTagMutabilityOutput {
	return o
}

func (o RepositoryImageTagMutabilityOutput) ToRepositoryImageTagMutabilityOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityOutput {
	return o
}

func (o RepositoryImageTagMutabilityOutput) ToRepositoryImageTagMutabilityPtrOutput() RepositoryImageTagMutabilityPtrOutput {
	return o.ToRepositoryImageTagMutabilityPtrOutputWithContext(context.Background())
}

func (o RepositoryImageTagMutabilityOutput) ToRepositoryImageTagMutabilityPtrOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v RepositoryImageTagMutability) *RepositoryImageTagMutability {
		return &v
	}).(RepositoryImageTagMutabilityPtrOutput)
}

func (o RepositoryImageTagMutabilityOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o RepositoryImageTagMutabilityOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryImageTagMutability) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o RepositoryImageTagMutabilityOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryImageTagMutabilityOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e RepositoryImageTagMutability) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type RepositoryImageTagMutabilityPtrOutput struct{ *pulumi.OutputState }

func (RepositoryImageTagMutabilityPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryImageTagMutability)(nil)).Elem()
}

func (o RepositoryImageTagMutabilityPtrOutput) ToRepositoryImageTagMutabilityPtrOutput() RepositoryImageTagMutabilityPtrOutput {
	return o
}

func (o RepositoryImageTagMutabilityPtrOutput) ToRepositoryImageTagMutabilityPtrOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityPtrOutput {
	return o
}

func (o RepositoryImageTagMutabilityPtrOutput) Elem() RepositoryImageTagMutabilityOutput {
	return o.ApplyT(func(v *RepositoryImageTagMutability) RepositoryImageTagMutability {
		if v != nil {
			return *v
		}
		var ret RepositoryImageTagMutability
		return ret
	}).(RepositoryImageTagMutabilityOutput)
}

func (o RepositoryImageTagMutabilityPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o RepositoryImageTagMutabilityPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *RepositoryImageTagMutability) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// RepositoryImageTagMutabilityInput is an input type that accepts RepositoryImageTagMutabilityArgs and RepositoryImageTagMutabilityOutput values.
// You can construct a concrete instance of `RepositoryImageTagMutabilityInput` via:
//
//          RepositoryImageTagMutabilityArgs{...}
type RepositoryImageTagMutabilityInput interface {
	pulumi.Input

	ToRepositoryImageTagMutabilityOutput() RepositoryImageTagMutabilityOutput
	ToRepositoryImageTagMutabilityOutputWithContext(context.Context) RepositoryImageTagMutabilityOutput
}

var repositoryImageTagMutabilityPtrType = reflect.TypeOf((**RepositoryImageTagMutability)(nil)).Elem()

type RepositoryImageTagMutabilityPtrInput interface {
	pulumi.Input

	ToRepositoryImageTagMutabilityPtrOutput() RepositoryImageTagMutabilityPtrOutput
	ToRepositoryImageTagMutabilityPtrOutputWithContext(context.Context) RepositoryImageTagMutabilityPtrOutput
}

type repositoryImageTagMutabilityPtr string

func RepositoryImageTagMutabilityPtr(v string) RepositoryImageTagMutabilityPtrInput {
	return (*repositoryImageTagMutabilityPtr)(&v)
}

func (*repositoryImageTagMutabilityPtr) ElementType() reflect.Type {
	return repositoryImageTagMutabilityPtrType
}

func (in *repositoryImageTagMutabilityPtr) ToRepositoryImageTagMutabilityPtrOutput() RepositoryImageTagMutabilityPtrOutput {
	return pulumi.ToOutput(in).(RepositoryImageTagMutabilityPtrOutput)
}

func (in *repositoryImageTagMutabilityPtr) ToRepositoryImageTagMutabilityPtrOutputWithContext(ctx context.Context) RepositoryImageTagMutabilityPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(RepositoryImageTagMutabilityPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(RepositoryEncryptionTypeOutput{})
	pulumi.RegisterOutputType(RepositoryEncryptionTypePtrOutput{})
	pulumi.RegisterOutputType(RepositoryImageTagMutabilityOutput{})
	pulumi.RegisterOutputType(RepositoryImageTagMutabilityPtrOutput{})
}
